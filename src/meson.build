pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'bookmarks')
gnome = import('gnome')

gnome.compile_resources('bookmarks',
  'bookmarks.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'bookmarks.in',
  output: 'bookmarks',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

bookmarks_sources = [
  'main.py',
  'window.py',
  'pages/BookMarks.py',
  'pages/Tags.py',
  'pages/Folders.py',
  'widgets/BookMarkCard.py',
  'widgets/FolderDisplay.py',
  'widgets/forms/QuickCreateBookMark.py',
  'widgets/DeleteBookMark.py',
  'widgets/forms/QuickCreateTag.py',
  'widgets/TagCard.py',
  'widgets/DeleteTag.py',
  'widgets/TagBadge.py',
  'widgets/forms/QuickCreateFolder.py',
  'widgets/FolderCard.py'
]

install_data(bookmarks_sources, install_dir: moduledir)
