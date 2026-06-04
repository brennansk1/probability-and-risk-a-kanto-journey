# =============================================================================
# Makefile -- build "Probability & Risk: A Kanto Journey"
# Markdown -> Pandoc -> self-contained HTML (+MathJax) -> WeasyPrint/Chrome PDF
# =============================================================================
#   make assets     Download sprites + generate figures
#   make figures    (Re)generate matplotlib figures and distribution cards
#   make embed      Inject <figure> blocks into chapters (idempotent)
#   make verify     Run numeric verification of every example (seed=151)
#   make lint       Run format/latex/sprite audit + coverage checks
#   make html       Build styled single-file HTML
#   make pdf         Build the print-and-bind PDF (WeasyPrint, falls back to Chrome)
#   make book       verify -> lint -> figures -> embed -> pdf  (full gated build)
#   make clean      Remove build artefacts
# =============================================================================

PANDOC      := pandoc
PYTHON      := python3

BOOK_DIR    := book
CH_DIR      := $(BOOK_DIR)/chapters
APX_DIR     := $(BOOK_DIR)/appendices
FRONT_DIR   := $(BOOK_DIR)/frontmatter
ASSETS_DIR  := assets
OUT_DIR     := build/output
CSS         := $(BOOK_DIR)/theme.css
PREAMBLE    := $(BOOK_DIR)/mathjax-preamble.md
TITLE_HTML  := $(FRONT_DIR)/title.html

# Inputs in reading order: math macros first, then front matter, chapters, appendices.
FRONT    := $(FRONT_DIR)/how-to-use.md $(FRONT_DIR)/diagnostic.md
CHAPTERS := $(sort $(wildcard $(CH_DIR)/ch*.md))
APPENDIX := $(sort $(wildcard $(APX_DIR)/appendix_*.md))
CONTENT  := $(PREAMBLE) $(FRONT) $(CHAPTERS) $(APPENDIX)

HTML_OUT := $(OUT_DIR)/kanto_journey.html
PDF_OUT  := $(OUT_DIR)/kanto_journey.pdf
WB_HTML  := $(OUT_DIR)/kanto_journey_workbook.html
WB_PDF   := $(OUT_DIR)/kanto_journey_workbook.pdf
MJ_CONFIG  := $(BOOK_DIR)/mathjax-config.html
WB_CSS     := $(BOOK_DIR)/workbook.css
WB_FILTER  := tools/workbook.lua

PANDOC_FLAGS := \
	--from=markdown+smart+tex_math_dollars+footnotes+fenced_divs+header_attributes \
	--standalone --embed-resources \
	--css=$(CSS) \
	--mathjax \
	--include-in-header=$(MJ_CONFIG) \
	--toc --toc-depth=2 \
	--resource-path=.:$(CH_DIR):$(APX_DIR):$(ASSETS_DIR):$(BOOK_DIR) \
	--include-before-body=$(TITLE_HTML) \
	--metadata title="Probability & Risk: A Kanto Journey"

.PHONY: all book assets figures embed verify lint html pdf workbook clean

all: pdf

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

assets:
	$(PYTHON) $(ASSETS_DIR)/download_sprites.py
	$(PYTHON) $(ASSETS_DIR)/download_real_assets.py
	$(MAKE) figures

figures:
	$(PYTHON) figures/src/generate_figures.py
	@for f in figures/src/gen_*.py; do echo "  -> $$f"; $(PYTHON) "$$f" || exit 1; done

embed:
	$(PYTHON) $(BOOK_DIR)/embed_visuals.py

verify:
	$(PYTHON) sims/verify_examples.py

lint:
	$(PYTHON) tools/check_format.py
	$(PYTHON) tools/check_coverage.py

html: $(HTML_OUT)
$(HTML_OUT): $(CONTENT) $(CSS) $(TITLE_HTML) | $(OUT_DIR)
	@echo "==> Building styled HTML..."
	$(PANDOC) $(PANDOC_FLAGS) -o $@ $(CONTENT)

pdf: $(PDF_OUT)
$(PDF_OUT): $(HTML_OUT)
	@echo "==> Rendering print-and-bind PDF..."
	@if command -v weasyprint >/dev/null 2>&1; then \
		echo "  using weasyprint"; \
		weasyprint $(HTML_OUT) $(PDF_OUT); \
	elif [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then \
		echo "  using Chrome headless (weasyprint not found)"; \
		"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
			--headless --disable-gpu --no-pdf-header-footer \
			--virtual-time-budget=60000 \
			--print-to-pdf="$$PWD/$(PDF_OUT)" "file://$$PWD/$(HTML_OUT)"; \
	else \
		echo "  ERROR: install weasyprint or Google Chrome"; exit 1; \
	fi
	@echo "==> PDF: $(PDF_OUT)"

# Full gated build: numbers verified, format audited, then compiled.
book: verify lint figures embed pdf

# ---------------------------------------------------------------------------
# Workbook edition (reMarkable): dot-grid work area after every problem.
# Non-destructive — same source, plus the Lua filter + workbook.css.
# ---------------------------------------------------------------------------
workbook: $(WB_PDF)
$(WB_HTML): $(CONTENT) $(CSS) $(WB_CSS) $(WB_FILTER) $(TITLE_HTML) $(MJ_CONFIG) | $(OUT_DIR)
	@echo "==> Building workbook HTML (work space after each problem)..."
	$(PANDOC) $(PANDOC_FLAGS) --css=$(WB_CSS) --lua-filter=$(WB_FILTER) -o $@ $(CONTENT)
$(WB_PDF): $(WB_HTML)
	@echo "==> Rendering workbook PDF..."
	@if command -v weasyprint >/dev/null 2>&1; then \
		weasyprint $(WB_HTML) $(WB_PDF); \
	elif [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then \
		"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
			--headless --disable-gpu --no-pdf-header-footer \
			--virtual-time-budget=90000 \
			--print-to-pdf="$$PWD/$(WB_PDF)" "file://$$PWD/$(WB_HTML)"; \
	else \
		echo "  ERROR: install weasyprint or Google Chrome"; exit 1; \
	fi
	@echo "==> Workbook PDF: $(WB_PDF)"

clean:
	rm -rf $(OUT_DIR)
