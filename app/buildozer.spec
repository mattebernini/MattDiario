[app]

title: MattDiario

package.name: MattDiario

package.domain: online.mattebernini

source.dir: .

source.include_exts: db, png, kv, py, env
source.exclude_exts: sh
source.exclude_dirs: bin
source.exclude_patterns: 
source.include_patterns: 

# version.regex =
# version.filename =
version = 1.0

requirements = kivy,sqlite3,datetime,webbrowser,os,requests,dotenv

presplash.filename: matt_diario.png

icon.filename: matt_diario.png

orientation: portrait

fullscreen: 1

home_app: 1
