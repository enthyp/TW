PACKAGE=traces
PACKAGE_DIR=src/$(PACKAGE)
TEST_DIR=tests
OUT_DIR=out

.PHONY: install
install:
	@pip install -e .

.PHONY: test
test:
	@pytest --log-cli-level=1 $(TEST_DIR)

.PHONY: clean
clean:
	@rm -rf \
        $(PACKAGE_DIR)/__pycache__ \
        $(TEST_DIR)/__pycache__ \
        $(TEST_DIR)/*.txt \
        $(TEST_DIR)/*.pdf \
        $(TEST_DIR)/out \
        $(OUT_DIR)
