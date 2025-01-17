ERROR_NO_ARGUMENT = $(error Must pass at least one argument)
.phony: err
err:
	$(ERROR_NO_ARGUMENT)

BUILD_DIR     = build
SRC_MAKE_CALL = $(MAKE) -f src/Makefile BUILD_DIR=$(BUILD_DIR) NO_CSS=$(NO_CSS)
ifdef LOCALE
	SRC_MAKE_CALL += LOCALE=$(LOCALE)
endif
ifdef VERSION
	SRC_MAKE_CALL += VERSION=$(VERSION)
endif

# For this target, only archive docsets that have already been built in BUILD_DIR
.phony: archive
archive: $(foreach docset,$(wildcard $(BUILD_DIR)/*.docset),$(basename $(docset)).tgz)

# For this target, simply remove all docsets and tgz files from BUILD_DIR
.phony: clean
clean:
	rm -rf $(BUILD_DIR)/*.docset $(BUILD_DIR)/*.tgz

# For this target, remove everything from tmp/
.phony: dist-clean
dist-clean: clean
	rm -rf tmp/*

# All supported docsets should be listed here
SUPPORTED_TARGETS = \
debmake \
Flex \
glibc \
GNU_Autoconf \
GNU_Autoconf_Archive \
GNU_Automake \
GNU_Bash \
GNU_Bison \
GNU_Coding_Standards \
GNU_Coreutils \
GNU_Guix \
GNU_Libtool \
GNU_Make \
ncurses

.phony: $(SUPPORTED_TARGETS)
$(SUPPORTED_TARGETS):
	$(SRC_MAKE_CALL) DOCSET_NAME=$@

.phony: all
all: $(SUPPORTED_TARGETS)

$(BUILD_DIR)/%.tgz: $(BUILD_DIR)/%.docset
	tar --exclude='.DS_Store' -czf $@ -C $(BUILD_DIR) $(notdir $(basename $@).docset)
