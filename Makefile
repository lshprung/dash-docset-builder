ERROR_NO_ARGUMENT = $(error Must pass at least one argument)
.phony: err
err:
	$(ERROR_NO_ARGUMENT)

BUILD_DIR     = build
SRC_MAKE_CALL = $(MAKE) -f src/Makefile BUILD_DIR=$(BUILD_DIR)

# For this target, only archive docsets that have already been built in BUILD_DIR
.phony: archive
archive:
	#TODO

# For this target, simply remove all docsets and tgz files from BUILD_DIR
.phony: clean
clean:
	rm -rf $(BUILD_DIR)/*.docset $(BUILD_DIR)/*.tgz

# All supported docsets should be listed here
.phony: GNU_Make
GNU_Make: $(BUILD_DIR)/GNU_Make.docset

# All docset files should be listed here
$(BUILD_DIR)/GNU_Make.docset: 
	$(SRC_MAKE_CALL) DOCSET_NAME=GNU_Make

# All archive files should be listed here
$(BUILD_DIR)/GNU_Make.tgz: GNU_Make
	tar --exclude='.DS_Store' -czf $@ $(BUILD_DIR)/GNU_Make.docset
