# Makefile should be called directly, passing the following arguments:
#   DOCSET_NAME = ... (should be a directory under ./configs)
#   optionally:
#     BUILD_DIR = ... (create built docsets under the directory BUILDDIR)

ERROR_DOCSET_NAME = $(error DOCSET_NAME is unset)
.phony: err

ifndef DOCSET_NAME
err: ; $(ERROR_DOCSET_NAME)
endif

SOURCE_DIR    = configs/$(DOCSET_NAME)
BUILD_DIR     = .
DOCSET_DIR    = $(BUILD_DIR)/$(DOCSET_NAME).docset
CONTENTS_DIR  = $(DOCSET_DIR)/Contents
RESOURCES_DIR = $(CONTENTS_DIR)/Resources
DOCUMENTS_DIR = $(RESOURCES_DIR)/Documents

INFO_PLIST_FILE = $(CONTENTS_DIR)/Info.plist
INDEX_FILE      = $(RESOURCES_DIR)/docSet.dsidx
ICON_FILE       = $(DOCSET_DIR)/icon.png
ARCHIVE_FILE    = $(DOCSET_NAME).tgz

SRC_INFO_PLIST_FILE = $(SOURCE_DIR)/Info.plist

DOCSET = $(INFO_PLIST_FILE) $(INDEX_FILE) $(ICON_FILE)

all: $(DOCSET)

ifdef DOCSET_NAME
include configs/$(DOCSET_NAME)/config.mk
endif

archive: $(ARCHIVE_FILE)

clean:
	rm -rf $(DOCSET_DIR) $(ARCHIVE_FILE)

tmp:
	mkdir -p $@

$(ARCHIVE_FILE): $(DOCSET)
	tar --exclude='.DS_Store' -czf $@ $(DOCSET_DIR)

$(DOCSET_DIR):
	mkdir -p $@

$(CONTENTS_DIR): $(DOCSET_DIR)
	mkdir -p $@

$(RESOURCES_DIR): $(CONTENTS_DIR)
	mkdir -p $@

$(INFO_PLIST_FILE): $(SRC_INFO_PLIST_FILE) $(CONTENTS_DIR)
	cp $(SRC_INFO_PLIST_FILE) $@

ifdef SRC_ICON_FILE
$(ICON_FILE): $(SRC_ICON_FILE) $(DOCSET_DIR)
	cp $(SRC_ICON_FILE) $@
endif
