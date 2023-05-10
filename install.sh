#!/bin/bash
APPID="moe.nyarchlinux.tour"
BUNDLENAME="nyarchtour.flatpak"
sudo flatpak-builder --install --force-clean flatpak-app "$APPID".json

if [ "$1" = "bundle" ]; then
	flatpak build-bundle ~/.local/share/flatpak/repo "$BUNDLENAME" "$APPID"
fi