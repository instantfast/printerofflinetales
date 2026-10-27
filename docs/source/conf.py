# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
# Website styling and chat
from pathlib import Path

_site_static = Path(__file__).resolve().parent / "_static"
_site_static.mkdir(parents=True, exist_ok=True)

_site_css = """
/* Article typography */
div.body,
.rst-content,
.bd-article {
    color: #283548;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 17px;
    line-height: 1.8;
    overflow-wrap: break-word;
}

div.body,
.wy-nav-content {
    background: #ffffff;
}

/* Main heading */
div.body h1,
.rst-content h1,
.bd-article h1 {
    color: #132c49;
    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 700;
    line-height: 1.3;
    margin: 0 0 26px;
    padding-bottom: 18px;
    border-bottom: 3px solid #1765ad;
}

/* Section headings */
div.body h2,
.rst-content h2,
.bd-article h2 {
    color: #132c49;
    background: #eef5fc;
    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(23px, 3vw, 28px);
    line-height: 1.4;
    margin: 36px 0 18px;
    padding: 12px 16px;
    border-left: 4px solid #1765ad;
    border-radius: 0 8px 8px 0;
}

/* Subheadings */
div.body h3,
.rst-content h3,
.bd-article h3 {
    color: #193e65;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 22px;
    line-height: 1.5;
    margin: 26px 0 12px;
}

/* Paragraphs and lists */
div.body p,
.rst-content p,
.bd-article p {
    margin-bottom: 20px;
    line-height: 1.85;
}

div.body li,
.rst-content li,
.bd-article li {
    margin-bottom: 10px;
}

div.body li > p,
.rst-content li > p,
.bd-article li > p {
    margin-bottom: 10px;
}

/* Article links */
div.body a,
.rst-content a,
.bd-article a {
    color: #1765ad;
    text-underline-offset: 3px;
}

div.body a:hover,
.rst-content a:hover,
.bd-article a:hover {
    color: #10487b;
}

a:focus-visible {
    outline: 3px solid #1765ad;
    outline-offset: 3px;
}

/* Images and code */
div.body img,
.rst-content img,
.bd-article img {
    max-width: 100%;
    height: auto;
}

div.body pre,
.rst-content pre,
.bd-article pre {
    overflow-x: auto;
    padding: 16px;
    background: #f5f7fa;
    border: 1px solid #dce5ef;
    border-radius: 8px;
}

/* Mobile */
@media (max-width: 767px) {
    div.body,
    .rst-content,
    .bd-article {
        font-size: 16px;
    }

    .wy-nav-content {
        padding: 24px 18px;
    }

    div.body h2,
    .rst-content h2,
    .bd-article h2 {
        margin-top: 28px;
        padding: 10px 12px;
    }

    div.body h3,
    .rst-content h3,
    .bd-article h3 {
        font-size: 20px;
    }
}
"""

(_site_static / "custom.css").write_text(
    _site_css,
    encoding="utf-8",
)

# Register CSS
html_static_path = list(globals().get("html_static_path", []))
if "_static" not in html_static_path:
    html_static_path.append("_static")

html_css_files = list(globals().get("html_css_files", []))
if "custom.css" not in html_css_files:
    html_css_files.append("custom.css")

# Register chat on every page
html_js_files = list(globals().get("html_js_files", []))
_site_chat_url = "https://code.jivosite.com/widget/cTI6R8IfQH"

if not any(
    (item[0] if isinstance(item, (tuple, list)) else item)
    == _site_chat_url
    for item in html_js_files
):
    html_js_files.append(
        (_site_chat_url, {"async": "async"})
    )
    
