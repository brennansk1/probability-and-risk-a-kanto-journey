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

PANDOC_FLAGS := \
	--from=markdown+smart+tex_math_dollars+footnotes+fenced_divs+header_attributes \
	--standalone --embed-resources \
	--css=$(CSS) \
	--mathjax \
	--toc --toc-depth=2 \
	--resource-path=.:$(CH_DIR):$(APX_DIR):$(ASSETS_DIR):$(BOOK_DIR) \
	--include-before-body=$(TITLE_HTML) \
	--metadata title="Probability & Risk: A Kanto Journey"

.PHONY: all book assets figures embed verify lint html pdf clean

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

clean:
	rm -rf $(OUT_DIR)
