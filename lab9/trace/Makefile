PACKAGE=traces
PACKAGE_DIR=$(PACKAGE)
TEST_DIR=tests

.PHONY: install
install:
	@pip install -e .

.PHONY: test
test:
	@pytest --log-cli-level=10 $(TEST_DIR)

.PHONY: clean
clean:
	@rm -rf $(PACKAGE).egg-info $(PACKAGE_DIR)/__pycache__ $(TEST_DIR)/__pycache__

