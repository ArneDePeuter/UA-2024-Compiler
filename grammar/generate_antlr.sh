current_dir=$(pwd)

if [ "$(basename "$current_dir")" != "grammar" ]; then
    cd ./grammar || exit 1
fi

java -jar antlr-4.13.1-complete.jar -o ../compiler/frontend/antlr_files -Dlanguage=Python3 Main.g4 -visitor
