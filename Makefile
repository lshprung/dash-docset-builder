ERROR_NO_ARGUMENT = $(error Must pass at least one argument)
.phony: err
err:
	$(ERROR_NO_ARGUMENT)

BUILD_DIR     = build
SRC_MAKE_CALL = $(MAKE) -f src/Makefile BUILD_DIR=$(BUILD_DIR) NO_CSS=$(NO_CSS) LOCALE=$(LOCALE)

# For this target, only archive docsets that have already been built in BUILD_DIR
.phony: archive
archive: $(foreach docset,$(wildcard $(BUILD_DIR)/*.docset),$(basename $(docset)).tgz)

# For this target, simply remove all docsets and tgz files from BUILD_DIR
.phony: clean
clean:
	rm -rf $(BUILD_DIR)/*.docset $(BUILD_DIR)/*.tgz

# All supported docsets should be listed here
SUPPORTED_TARGETS = \
debmake \
flex \
GNU_Make

.phony: $(SUPPORTED_TARGETS)
$(SUPPORTED_TARGETS):
	$(SRC_MAKE_CALL) DOCSET_NAME=$@

$(BUILD_DIR)/%.tgz: $(BUILD_DIR)/%.docset
	tar --exclude='.DS_Store' -czf $@ $(basename $@).docset
