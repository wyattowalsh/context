"""context/enums.py 
"""

from enum import Enum, unique


class OutputType(Enum): 
    """Output type for the context module"""
    TEXT     = "text"
    MARKDOWN = "markdown"
    HTML     = "html"
    JSON     = "json"
    XML      = "xml"


class OutputFileExtension(Enum): 
    """Output file extension for the context module"""
    TEXT     = "txt"
    MARKDOWN = "md"
    HTML     = "html"
    JSON     = "json"
    XML      = "xml"


@unique
class FileType(Enum): 
    """
    Exhaustive canonical file‑types for large‑scale web–scraping pipelines.

    ── Conventions ─────────────────────────────────────────────────────────
    • Members are grouped by broad media / usage category for clarity.
    • Each value is the lowercase extension exactly as it appears on disk.
    • Compound extensions (e.g. “tar.gz”) are expressed literally.
    • Names never start with a digit; leading underscores are used when needed.
    """

    # ── Plain & Markup Text ───────────────────────────────────────────────
    TEXT     = "txt"
    MARKDOWN = "md"
    RST      = "rst"
    ASCIIDOC = "adoc"
    ORG      = "org"
    HTML     = "html"
    XHTML    = "xhtml"
    XML      = "xml"

    # ── Configuration & Metadata ──────────────────────────────────────────
    JSON       = "json"
    JSONL      = "jsonl"
    YAML       = "yaml"
    YML        = "yml"
    TOML       = "toml"
    INI        = "ini"
    CFG        = "cfg"
    CONF       = "conf"
    ENV        = "env"
    PROPERTIES = "properties"

    # ── Code & Scripts ────────────────────────────────────────────────────
    PY     = "py"
    IPYNB  = "ipynb"
    JS     = "js"
    JSX    = "jsx"
    TS     = "ts"
    TSX    = "tsx"
    JAVA   = "java"
    C      = "c"
    H      = "h"
    CPP    = "cpp"
    HPP    = "hpp"
    CS     = "cs"
    GO     = "go"
    RS     = "rs"
    SWIFT  = "swift"
    KT     = "kt"
    SH     = "sh"
    BASH   = "bash"
    ZSH    = "zsh"
    BAT    = "bat"
    PS1    = "ps1"
    RB     = "rb"
    PHP    = "php"
    PL     = "pl"
    LUA    = "lua"
    R      = "r"
    M      = "m"          # MATLAB / Objective‑C
    JL     = "jl"
    SCALA  = "scala"
    CLJ    = "clj"
    GROOVY = "groovy"
    DART   = "dart"
    SQL    = "sql"
    WASM   = "wasm"

    # ── Data Serialization & Interchange ─────────────────────────────────
    CSV     = "csv"
    TSV     = "tsv"
    PARQUET = "parquet"
    AVRO    = "avro"
    ORC     = "orc"
    ARROW   = "arrow"
    FEATHER = "feather"
    PKL     = "pkl"
    HDF     = "hdf"
    H5      = "h5"
    NPZ     = "npz"
    NPY     = "npy"
    MAT     = "mat"
    MSGPACK = "msgpack"

    # ── Documents ────────────────────────────────────────────────────────
    PDF   = "pdf"
    DOC   = "doc"
    DOCX  = "docx"
    RTF   = "rtf"
    ODT   = "odt"
    WPD   = "wpd"
    TEX   = "tex"
    LATEX = "latex"
    BIB   = "bib"
    PAGES = "pages"

    # ── Spreadsheets & Tabular Data ──────────────────────────────────────
    XLS  = "xls"
    XLSX = "xlsx"
    ODS  = "ods"

    # ── Presentations ────────────────────────────────────────────────────
    PPT  = "ppt"
    PPTX = "pptx"
    ODP  = "odp"
    KEY  = "key"          # Apple Keynote

    # ── eBooks & Publishing ──────────────────────────────────────────────
    EPUB = "epub"
    MOBI = "mobi"
    AZW3 = "azw3"
    FB2  = "fb2"
    IBKS = "ibooks"

    # ── Images (Raster) ──────────────────────────────────────────────────
    PNG  = "png"
    JPG  = "jpg"
    JPEG = "jpeg"
    GIF  = "gif"
    BMP  = "bmp"
    TIFF = "tiff"
    TIF  = "tif"
    WEBP = "webp"
    HEIC = "heic"
    HEIF = "heif"
    PSD  = "psd"
    ICO  = "ico"
    RAW  = "raw"
    CR2  = "cr2"
    NEF  = "nef"
    DNG  = "dng"
    ARW  = "arw"

    # ── Images (Vector) ──────────────────────────────────────────────────
    SVG        = "svg"
    AI         = "ai"
    EPS        = "eps"
    PS         = "ps"
    PDF_VECTOR = "pdf"   # duplicate ext intentionally disambiguated by name

    # ── Audio ────────────────────────────────────────────────────────────
    MP3  = "mp3"
    WAV  = "wav"
    AAC  = "aac"
    FLAC = "flac"
    OGG  = "ogg"
    OPUS = "opus"
    M4A  = "m4a"
    WMA  = "wma"
    AIFF = "aiff"
    MID  = "mid"
    MIDI = "midi"
    AMR  = "amr"

    # ── Video ────────────────────────────────────────────────────────────
    MP4   = "mp4"
    M4V   = "m4v"
    MOV   = "mov"
    AVI   = "avi"
    MKV   = "mkv"
    WEBM  = "webm"
    FLV   = "flv"
    SWF   = "swf"
    WMV   = "wmv"
    MPEG  = "mpeg"
    MPG   = "mpg"
    MPEG2 = "mpeg2"
    MPEG4 = "mpeg4"
    TS    = "ts"
    M2TS  = "m2ts"
    3GP   = "3gp"
    3G2   = "3g2"
    OGV   = "ogv"
    ASF   = "asf"
    F4V   = "f4v"

    # ── 3D & CAD Assets ─────────────────────────────────────────────────
    OBJ   = "obj"
    STL   = "stl"
    PLY   = "ply"
    GLTF  = "gltf"
    GLB   = "glb"
    DAE   = "dae"
    FBX   = "fbx"
    _3DS  = "3ds"
    DXF   = "dxf"
    DWG   = "dwg"
    BLEND = "blend"
    SKP   = "skp"

    # ── Fonts & Icons ────────────────────────────────────────────────────
    TTF      = "ttf"
    OTF      = "otf"
    WOFF     = "woff"
    WOFF2    = "woff2"
    EOT      = "eot"
    PFA      = "pfa"
    PFB      = "pfb"
    ICO_FONT = "icns"

    # ── Archives & Compression ───────────────────────────────────────────
    ZIP     = "zip"
    TAR     = "tar"
    TGZ     = "tgz"
    TAR_GZ  = "tar.gz"
    TAR_BZ2 = "tar.bz2"
    TAR_XZ  = "tar.xz"
    GZ      = "gz"
    BZ2     = "bz2"
    XZ      = "xz"
    LZ      = "lz"
    LZMA    = "lzma"
    ZSTD    = "zst"
    _7Z     = "7z"
    RAR     = "rar"
    CAB     = "cab"
    AR      = "ar"
    JAR     = "jar"
    WAR     = "war"
    EAR     = "ear"

    # ── Disk Images ──────────────────────────────────────────────────────
    ISO   = "iso"
    IMG   = "img"
    DMG   = "dmg"
    VMDK  = "vmdk"
    VDI   = "vdi"
    QCOW2 = "qcow2"

    # ── Packages & Installers ────────────────────────────────────────────
    DEB      = "deb"
    RPM      = "rpm"
    APK      = "apk"
    PKG      = "pkg"
    MSI      = "msi"
    EXE_PKG  = "exe"      # installer executable
    APPIMAGE = "appimage"
    SNAP     = "snap"
    FLATPAK  = "flatpak"
    DMG_PKG  = "dmg"      # macOS pkg-in‑dmg

    # ── Executables & Libraries ──────────────────────────────────────────
    EXE   = "exe"
    DLL   = "dll"
    SO    = "so"
    DYLIB = "dylib"
    BIN   = "bin"
    ELF   = "elf"
    IPA   = "ipa"
    A     = "a"
    LIB   = "lib"

    # ── Database Files & Dumps ───────────────────────────────────────────
    SQLITE   = "sqlite"
    SQLITE3  = "sqlite3"
    DB       = "db"
    MDB      = "mdb"
    ACCDB    = "accdb"
    DBF      = "dbf"
    FDB      = "fdb"
    SQL_DUMP = "sql.gz"

    # ── Geospatial & GIS ────────────────────────────────────────────────
    SHP          = "shp"
    SHX          = "shx"
    GEOJSON      = "geojson"
    KML          = "kml"
    KMZ          = "kmz"
    GPX          = "gpx"
    GPKG         = "gpkg"
    TIFF_GEOTIFF = "tif"   # GeoTIFF uses .tif/.tiff
    TOPOJSON     = "topojson"
    OSM          = "osm"

    # ── Scientific & Specialized Data ───────────────────────────────────
    FITS   = "fits"
    CDF    = "cdf"
    GRIB   = "grib"
    NETCDF = "nc"
    HDF5   = "hdf5"
    MZML   = "mzml"
    MGF    = "mgf"
    PDB    = "pdb"
    CIF    = "cif"
    MMCIF  = "mmcif"

    # ── Logs & Traces ───────────────────────────────────────────────────
    LOG = "log"
    HAR = "har"

    # ── Certificates & Keys ─────────────────────────────────────────────
    PEM = "pem"
    CRT = "crt"
    CER = "cer"
    DER = "der"
    KEY = "key"
    PFX = "pfx"
    P12 = "p12"
    ASC = "asc"
    SIG = "sig"

    # ── BitTorrent & Shortcuts ──────────────────────────────────────────
    TORRENT = "torrent"
    URL     = "url"
    WEBLOC  = "webloc"
    LNK     = "lnk"


@unique
@unique
class FileGroup(Enum): 
    """
    Canonical high‑level groupings of file types encountered during
    web‑scale scraping and content processing.
    """

    TEXT          = "text_plain_markup"
    CONFIG        = "configuration_metadata"
    CODE          = "code_scripts"
    SERIALIZATION = "data_serialization_interchange"
    DOCUMENT      = "documents"
    SPREADSHEET   = "spreadsheets_tabular"
    PRESENTATION  = "presentations"
    EBOOK         = "ebooks_publishing"
    IMAGE_RASTER  = "images_raster"
    IMAGE_VECTOR  = "images_vector"
    AUDIO         = "audio"
    VIDEO         = "video"
    THREE_D       = "3d_cad_assets"
    FONT_ICON     = "fonts_icons"
    ARCHIVE       = "archives_compressed"
    DISK_IMAGE    = "disk_images"
    INSTALLER     = "packages_installers"
    EXECUTABLE    = "executables_libraries"
    DATABASE      = "database_files_dumps"
    GIS           = "geospatial_gis"
    SCIENTIFIC    = "scientific_specialized"
    LOG           = "logs_traces"
    CERTIFICATE   = "certificates_keys"
    BITTORRENT    = "bittorrent_payloads"
    SHORTCUT      = "shortcuts_links"