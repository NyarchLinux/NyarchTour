application_id = 'moe.nyarchlinux.tour'

scalable_dir = join_paths('hicolor', 'scalable', 'apps')
install_data(
  join_paths(scalable_dir, ('@0@.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

symbolic_dir = join_paths('hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, ('@0@-symbolic.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)
symbolic_dir = join_paths(get_option('datadir'), 'icons/hicolor/symbolic/apps')
install_data (
    'custom-icons/nyarch-logo.svg',
    install_dir: symbolic_dir
)
install_data (
    'custom-icons/komikku-screenshots.svg',
    install_dir: symbolic_dir
)
install_data (
    'custom-icons/open-in-new.svg',
    install_dir: symbolic_dir
)
install_data (
    'custom-icons/web.svg',
    install_dir: symbolic_dir
)