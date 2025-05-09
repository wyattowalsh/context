"""context/utils.py -- utility functions module
"""

from context.enums import FileGroup, FileType

FILE_GROUP_TYPE_MAP = {
    FileGroup.TEXT:
    frozenset({
        FileType.TEXT,
        FileType.MARKDOWN,
        FileType.RST,
        FileType.ASCIIDOC,
        FileType.ORG,
        FileType.HTML,
        FileType.XHTML,
        FileType.XML,
    }),
    FileGroup.CONFIG:
    frozenset({
        FileType.JSON,
        FileType.JSONL,
        FileType.YAML,
        FileType.YML,
        FileType.TOML,
        FileType.INI,
        FileType.CFG,
        FileType.CONF,
        FileType.ENV,
        FileType.PROPERTIES,
    }),
    FileGroup.CODE:
    frozenset({
        FileType.PY,
        FileType.IPYNB,
        FileType.JS,
        FileType.JSX,
        FileType.TS,
        FileType.TSX,
        FileType.JAVA,
        FileType.C,
        FileType.H,
        FileType.CPP,
        FileType.HPP,
        FileType.CS,
        FileType.GO,
        FileType.RS,
        FileType.SWIFT,
        FileType.KT,
        FileType.SH,
        FileType.BASH,
        FileType.ZSH,
        FileType.BAT,
        FileType.PS1,
        FileType.RB,
        FileType.PHP,
        FileType.PL,
        FileType.LUA,
        FileType.R,
        FileType.M,
        FileType.JL,
        FileType.SCALA,
        FileType.CLJ,
        FileType.GROOVY,
        FileType.DART,
        FileType.SQL,
        FileType.WASM,
    }),
    FileGroup.SERIALIZATION:
    frozenset({
        FileType.CSV,
        FileType.TSV,
        FileType.PARQUET,
        FileType.AVRO,
        FileType.ORC,
        FileType.ARROW,
        FileType.FEATHER,
        FileType.PKL,
        FileType.HDF,
        FileType.H5,
        FileType.NPZ,
        FileType.NPY,
        FileType.MAT,
        FileType.MSGPACK,
    }),
    FileGroup.DOCUMENT:
    frozenset({
        FileType.PDF,
        FileType.DOC,
        FileType.DOCX,
        FileType.RTF,
        FileType.ODT,
        FileType.WPD,
        FileType.TEX,
        FileType.LATEX,
        FileType.BIB,
        FileType.PAGES,
    }),
    FileGroup.SPREADSHEET:
    frozenset({FileType.XLS, FileType.XLSX, FileType.ODS}),
    FileGroup.PRESENTATION:
    frozenset({FileType.PPT, FileType.PPTX, FileType.ODP, FileType.KEY}),
    FileGroup.EBOOK:
    frozenset({
        FileType.EPUB, FileType.MOBI, FileType.AZW3, FileType.FB2,
        FileType.IBKS
    }),
    FileGroup.IMAGE_RASTER:
    frozenset({
        FileType.PNG,
        FileType.JPG,
        FileType.JPEG,
        FileType.GIF,
        FileType.BMP,
        FileType.TIFF,
        FileType.TIF,
        FileType.WEBP,
        FileType.HEIC,
        FileType.HEIF,
        FileType.PSD,
        FileType.ICO,
        FileType.RAW,
        FileType.CR2,
        FileType.NEF,
        FileType.DNG,
        FileType.ARW,
    }),
    FileGroup.IMAGE_VECTOR:
    frozenset({
        FileType.SVG, FileType.AI, FileType.EPS, FileType.PS,
        FileType.PDF_VECTOR
    }),
    FileGroup.AUDIO:
    frozenset({
        FileType.MP3,
        FileType.WAV,
        FileType.AAC,
        FileType.FLAC,
        FileType.OGG,
        FileType.OPUS,
        FileType.M4A,
        FileType.WMA,
        FileType.AIFF,
        FileType.MID,
        FileType.MIDI,
        FileType.AMR,
    }),
    FileGroup.VIDEO:
    frozenset({
        FileType.MP4,
        FileType.M4V,
        FileType.MOV,
        FileType.AVI,
        FileType.MKV,
        FileType.WEBM,
        FileType.FLV,
        FileType.SWF,
        FileType.WMV,
        FileType.MPEG,
        FileType.MPG,
        FileType.MPEG2,
        FileType.MPEG4,
        FileType.TS,
        FileType.M2TS,
        FileType._3GP,
        FileType._3G2,
        FileType.OGV,
        FileType.ASF,
        FileType.F4V,
    }),
    FileGroup.THREE_D:
    frozenset({
        FileType.OBJ,
        FileType.STL,
        FileType.PLY,
        FileType.GLTF,
        FileType.GLB,
        FileType.DAE,
        FileType.FBX,
        FileType._3DS,
        FileType.DXF,
        FileType.DWG,
        FileType.BLEND,
        FileType.SKP,
    }),
    FileGroup.FONT_ICON:
    frozenset({
        FileType.TTF,
        FileType.OTF,
        FileType.WOFF,
        FileType.WOFF2,
        FileType.EOT,
        FileType.PFA,
        FileType.PFB,
        FileType.ICO_FONT,
    }),
    FileGroup.ARCHIVE:
    frozenset({
        FileType.ZIP,
        FileType.TAR,
        FileType.TGZ,
        FileType.TAR_GZ,
        FileType.TAR_BZ2,
        FileType.TAR_XZ,
        FileType.GZ,
        FileType.BZ2,
        FileType.XZ,
        FileType.LZ,
        FileType.LZMA,
        FileType.ZSTD,
        FileType._7Z,
        FileType.RAR,
        FileType.CAB,
        FileType.AR,
        FileType.JAR,
        FileType.WAR,
        FileType.EAR,
    }),
    FileGroup.DISK_IMAGE:
    frozenset({
        FileType.ISO, FileType.IMG, FileType.DMG, FileType.VMDK, FileType.VDI,
        FileType.QCOW2
    }),
    FileGroup.INSTALLER:
    frozenset({
        FileType.DEB,
        FileType.RPM,
        FileType.APK,
        FileType.PKG,
        FileType.MSI,
        FileType.EXE_PKG,
        FileType.APPIMAGE,
        FileType.SNAP,
        FileType.FLATPAK,
        FileType.DMG_PKG,
    }),
    FileGroup.EXECUTABLE:
    frozenset({
        FileType.EXE,
        FileType.DLL,
        FileType.SO,
        FileType.DYLIB,
        FileType.BIN,
        FileType.ELF,
        FileType.IPA,
        FileType.A,
        FileType.LIB,
    }),
    FileGroup.DATABASE:
    frozenset({
        FileType.SQLITE, FileType.SQLITE3, FileType.DB, FileType.MDB,
        FileType.ACCDB, FileType.DBF, FileType.FDB, FileType.SQL_DUMP
    }),
    FileGroup.GIS:
    frozenset({
        FileType.SHP,
        FileType.SHX,
        FileType.GEOJSON,
        FileType.KML,
        FileType.KMZ,
        FileType.GPX,
        FileType.GPKG,
        FileType.TIFF_GEOTIFF,
        FileType.TOPOJSON,
        FileType.OSM,
    }),
    FileGroup.SCIENTIFIC:
    frozenset({
        FileType.FITS,
        FileType.CDF,
        FileType.GRIB,
        FileType.NETCDF,
        FileType.HDF5,
        FileType.MZML,
        FileType.MGF,
        FileType.PDB,
        FileType.CIF,
        FileType.MMCIF,
    }),
    FileGroup.LOG:
    frozenset({FileType.LOG, FileType.HAR}),
    FileGroup.CERTIFICATE:
    frozenset({
        FileType.PEM,
        FileType.CRT,
        FileType.CER,
        FileType.DER,
        FileType.KEY,
        FileType.PFX,
        FileType.P12,
        FileType.ASC,
        FileType.SIG,
    }),
    FileGroup.BITTORRENT:
    frozenset({FileType.TORRENT}),
    FileGroup.SHORTCUT:
    frozenset({FileType.URL, FileType.WEBLOC, FileType.LNK}),
}


def get_file_group(file_type: FileType) -> FileGroup:
    """Get the file group for a given file type"""
    for file_group, file_types in FILE_GROUP_TYPE_MAP.items():
        if file_type in file_types:
            return file_group
    raise ValueError(f"No file group found for file type: {file_type}")


def get_file_groups(file_types: list[FileType]) -> list[FileGroup]:
    """Get the file groups for a given list of file types"""
    return [get_file_group(file_type) for file_type in file_types]


def get_file_type(file_group: FileGroup) -> list[FileType]:
    """Get the file types for a given file group"""
    return FILE_GROUP_TYPE_MAP[file_group]


def get_file_types(file_groups: list[FileGroup]) -> list[FileType]:
    """Get the file types for a given list of file groups"""
    return [get_file_type(file_group) for file_group in file_groups]


def get_file_group_type_map() -> dict[FileGroup, frozenset[FileType]]:
    """Get the file group type map"""
    return FILE_GROUP_TYPE_MAP


BLACKLIST_ROUTE_GLOBS: list[str] = [

    # ── admin & control panels ───────────────────────────────
    "**/admin*/**",
    "**/wp-admin/**",
    "**/dashboard/**",
    "**/manager/**",
    "**/panel/**",
    "**/console/**",
    "**/siteadmin/**",
    "**/cms/**",

    # ── authentication & user account flows ─────────────────
    "**/login**",
    "**/signin**",
    "**/logout**",
    "**/signout**",
    "**/signup**",
    "**/register**",
    "**/user/**",
    "**/account/**",
    "**/profile/**",
    "**/settings/**",
    "**/preferences/**",
    "**/password/**",
    "**/reset*password**",
    "**/forgot*password**",
    "**/oauth/**",
    "**/sso/**",

    # ── commerce & transactions ─────────────────────────────
    "**/cart/**",
    "**/checkout/**",
    "**/payment/**",
    "**/billing/**",
    "**/order*/**",
    "**/invoice*/**",
    "**/wishlist/**",
    "**/favorites/**",
    "**/compare/**",

    # ── static asset & build directories (not individual files) ─────────
    "**/static/**",
    "**/assets/**",
    "**/public/**",
    "**/dist/**",
    "**/build/**",
    "**/vendor/**",
    "**/node_modules/**",
    "**/bower_components/**",
    "**/_next/**",
    "**/__next/**",
    "**/_nuxt/**",
    "**/fonts/**",
    "**/css/**",
    "**/js/**",
    "**/script/**",
    "**/scripts/**",
    "**/img/**",
    "**/images/**",
    "**/media/**",
    "**/video/**",
    "**/audio/**",
    "**/uploads/**",
    "**/upload/**",
    "**/wp-content/**",
    "**/wp-includes/**",
    "**/staticfiles/**",

    # ── machine‑control, plumbing, & API endpoints ──────────
    "**/robots.txt",
    "**/sitemap*.xml",
    "**/ads.txt",
    "**/service-worker.js",
    "**/manifest.json",
    "**/browserconfig.xml",
    "**/humans.txt",
    "**/api/**",
    "**/graphql/**",
    "**/socket.io/**",
    "**/ws/**",
    "**/websocket/**",
    "**/swagger*/**",
    "**/openapi*/**",
    "**/v[0-9]*/**",  # generic versioned API roots

    # ── CGI & legacy entry points ───────────────────────────
    "**/cgi-bin/**",
    "**/*.cgi",
    "**/*.pl",
    "**/xmlrpc.php",

    # ── alternate views, embeds, & previews ─────────────────
    "**/amp/**",
    "**/*/amp",
    "**/*?amp=*",
    "**/print/**",
    "**/*print*",
    "**/*format=print*",
    "**/preview/**",
    "**/*preview=*",
    "**/embed/**",
    "**/*embed*",
    "**/oembed*",

    # ── social / interaction pages ──────────────────────────
    "**/share/**",
    "**/share*",
    "**/like/**",
    "**/comment*/**",
    "**/comments/**",
    "**/reply/**",

    # ── marketing, tracking, & analytics ────────────────────
    "**/ads/**",
    "**/ad*/**",
    "**/analytics/**",
    "**/banner/**",
    "**/promo/**",
    "**/pixel/**",
    "**/tracking/**",
    "*?utm_*",
    "*?yclid=*",
    "*?fbclid=*",
    "*?gclid=*",
    "*?icid=*",
    "*?mc_eid=*",
    "*?session*",
    "*?phpsessid=*",

    # ── legal / policy pages ────────────────────────────────
    "**/privacy/**",
    "**/terms/**",
    "**/policy/**",
    "**/cookie*/**",
    "**/cookies/**",

    # ── status / error / maintenance pages ──────────────────
    "**/status/**",
    "**/error/**",
    "**/404*",
    "**/403*",
    "**/500*",
    "**/maintenance/**",
    "**/coming-soon/**",
    "**/under-construction/**",

    # ── staging / test / dev / backups ──────────────────────
    "**/staging/**",
    "**/test/**",
    "**/beta/**",
    "**/sandbox/**",
    "**/dev/**",
    "**/debug/**",
    "**/qa/**",
    "**/old/**",
    "**/archive/**",
    "**/backup/**",
    "**/bak/**",
    "**/temp/**",
    "**/tmp/**",
    "**/cache/**",
    "**/logs/**",

    # ── taxonomy & pagination noise ─────────────────────────
    "**/tag/**",
    "**/tags/**",
    "**/category/**",
    "**/categories/**",
    "**/archive/**",
    "**/page/**",
    "**/p/**",
    "*?page=*",
    "*?per_page=*",
    "*?offset=*",
    "*?limit=*",
    "*?sort=*",
    "*?order=*",
    "*?filter=*",

    # ── download & file‑bucket routes (not file patterns) ───
    "**/download/**",
    "**/downloads/**",
    "**/file/**",
    "**/files/**",
    "**/attachment*/**",
    "**/attachments/**",
    "**/cdn-cgi/**",
    "**/cloudflare/**",
    "**/akamai/**",

    # ── redirection & outbound hops ─────────────────────────
    "**/redirect/**",
    "**/out/**",
    "**/go/**",
    "**/link/**",

    # ── newsletter & email subscription flows ───────────────
    "**/newsletter/**",
    "**/subscribe/**",
    "**/subscription/**",
    "**/unsubscribe/**",
    "**/email/**",

    # ── favicon & minor boilerplate assets ──────────────────
    "**/favicon.ico",
    "**/apple-touch-icon*",

    # ── misc repository & well‑known dirs ───────────────────
    "**/__pycache__/**",
    "**/.git/**",
    "**/.svn/**",
    "**/.hg/**",
    "**/.well-known/**",
]
