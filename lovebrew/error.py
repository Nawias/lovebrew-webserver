from enum import Enum, auto


class Error(Enum):
    # No valid package data sent
    NO_CONTENT_PACKAGE = 0
    # Packaged content is not a zip file
    CONTENT_NON_ZIP_FILE = auto()
    # Could not find 'lovebrew.toml' in the package
    MISSING_CONFIG_FILE = auto()
    # Could not find 'game.zip' in the package
    MISSING_GAME_CONTENT = auto()
    # Target is not valid
    TARGET_NOT_VALID = auto()
    # Command argument key invalid
    COMMAND_ARGUMENT_NOT_FOUND = auto()
    # Command failure
    COMMAND_FAILED = auto()
    # EXE not found
    COMMAND_EXE_NOT_FOUND = auto()
    # Invalid version info
    INVALID_VERSION_SPECIFIED = auto()
    # Outdated config file
    OUTDATED_CONFIG = auto()
    # Invalid config data
    INVALID_CONFIG_DATA = auto()
    # Wii U not allowed
    CAFE_INVALID_ON_APP_VERSION_2 = auto()
    # Invalid permission, use website
    INVALID_METHOD_USE_WEBSITE = auto()
    # Config version is mismatched
    CONFIG_VERSION_MISMATCH = auto()
    # Content zip is too large
    CONTENT_ZIP_TOO_LARGE = auto()
    # No error
    NONE = auto()

    def __str__(self):
        return self.name
