#!/usr/bin/env bash

echo "[+] Looking for dependencies..."

updatedb


if ![[ $(locate Aut2exe.exe) ]]; then
    echo "[+] Everything is installed."
else
    echo "[-] Autoit is "
fi
