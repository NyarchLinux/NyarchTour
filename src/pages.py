import subprocess
def btrfs_fs():
    try:
        script = """if [ "$(findmnt -n -o FSTYPE /)" == "btrfs" ]; then
          echo 1
        else
          echo 0
        fi
        """
        out = subprocess.check_output(["flatpak-spawn", "--host", "bash", "-c", script]).decode("utf-8")
        out = out.strip()
        if out == "1":
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

PAGES = [
	{
		"icon": "nyarch-logo",
		"title": "Welcome to Nyarch",
		"icon-size": 400,
		"body": "Nyarch Linux is an Arch Linux-based OS that aims to create the best possible experience for weebs.",
		"buttons": [
			{
				"label": "Open Website",
				"icon": None,
				"style": "suggested-action",
				"command": "xdg-open https://nyarchlinux.moe"
			}
		]
	},
	{
		"icon": "material_you_screenshot",
		"icon-size": 400,
		"title": "Material You",
		"body": "Choose any waifu as your wallpaper! The desktop and application themes automatically adjust their colors to make you feel at home. This is achieved by a modified version of the Material You Gnome extension.",
		"buttons": [
			{
				"label": "Open Settings",
				"icon": None,
				"style": "suggested-action",
				"command": "gnome-control-center background "
			}
		]
	},
	{
		"icon": "nyarchcustomize-screenshots",
		"icon-size": 400,
		"title": "Nyarch Customize",
		"body": "Change your layout quickly and customize animations and appearance.",
		"buttons": [
			{
				"label": "Open Nyarch Customize",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.customize"
			}
		]
	},
	{
		"icon": "tweaks-screenshots",
		"icon-size": 400,
		"title": "Need advanced customization?",
		"body": "You can further customize your operating system by editing configurations in Gnome Tweaks and installing new extensions in the Extension Manager.",
		"buttons": [
			{
				"label": "Open Tweaks",
				"icon": None,
				"style": "suggested-action",
				"command": "gnome-tweaks"
			},
			{
				"label": "Open Extension Manager",
				"icon": None,
				"style": "suggested-action",
				"command": "extension-manager"
			},
		]
	},
	{
		"icon": "catgirldownloader-screenshots",
		"icon-size": 400,
		"title": "Catgirl Downloader",
		"body": "This application satisfies one of the most important needs a weeb has: getting random pictures of cute cat girls whenever you want!",
		"buttons": [
			{
				"label": "Open Catgirl Downloader",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.catgirldownloader"
			}
		]
	},
	{
		"icon": "waifudownloader-screenshots",
		"icon-size": 400,
		"title": "Waifu Downloader",
		"body": "This application satisfies one of the most important needs a weeb has: getting random pictures of cute anime girls whenever you want!",
		"buttons": [
			{
				"label": "Open Waifu Downloader",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.waifudownloader"
			}
		]
	},
	{
		"icon": "komikku-screenshots",
		"icon-size": 400,
		"title": "Read manga with Komikku",
		"body": "Komikku is an amazing open source application for reading manga from the internet.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://valos.gitlab.io/Komikku/"
			},
			{
				"label": "Open Komikku",
				"icon": None,
				"style": "suggested-action",
				"command": "komikku"
			}
		]
	},
	{
		"icon": "shortwave-screenshots",
		"icon-size": 400,
		"title": "Listen to your favourite weeb radio with Shortwave",
		"body": "Shortwave is an Internet radio player that provides access to a station database with over 30,000 stations.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://gitlab.gnome.org/World/Shortwave"
			},
			{
				"label": "Open Shortwave",
				"icon": None,
				"style": "suggested-action",
				"command": "shortwave"
			}
		]
	},
	{
		"icon": "fragments-screenshots",
		"icon-size": 400,
		"title": "Download Torrents with Fragments",
		"body": "Fragments is an easy-to-use BitTorrent client. It can be used to transfer files via the BitTorrent protocol.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://gitlab.gnome.org/World/Fragments"
			},
			{
				"label": "Open Fragments",
				"icon": None,
				"style": "suggested-action",
				"command": "fragments"
			}
		]
	},
	{
		"icon": "lollypop-screenshots",
		"icon-size": 400,
		"title": "Listen to music with Lollypop",
		"body": "Lollypop is an amazingly lightweight music player with a party mode for streaming music from the Internet or playing music from your own collection.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://wiki.gnome.org/Apps/Lollypop"
			},
			{
				"label": "Open Lollypop",
				"icon": None,
				"style": "suggested-action",
				"command": "lollypop"
			}
		]
	},
	{
		"icon": "webapps-screenshots",
		"icon-size": 400,
		"title": "Turn your favorite (streaming) websites into apps",
		"body": "With the Webapp Manager, you can create applications from websites that integrate into your desktop. It supports extensions and many browsers.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://github.com/linuxmint/webapp-manager"
			},
			{
				"label": "Open Webapp Manager",
				"icon": None,
				"style": "suggested-action",
				"command": "webapp-manager"
			}
		]
	},
	{
		"icon": "software-screenshots",
		"icon-size": 400,
		"title": "Need other apps?",
		"body": "Download your favorite applications from an extensive catalog of applications with Gnome Software.",
		"buttons": [
			{
				"label": "Open Gnome Software",
				"icon": None,
				"style": "suggested-action",
				"command": "gnome-software"
			}
		]
	},
	{
		"icon": "nyarchwizard-screenshots",
		"icon-size": 400,
		"title": "Need suggestions?",
		"body": "The Nyarch Wizard will suggest some software to get you started with Nyarch Linux.",
		"buttons": [
			{
				"label": "Open Nyarch Wizard",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.wizard"
			}
		]
	},
	{
		"icon": "terminal-screenshots",
		"icon-size": 400,
		"title": "I use Nyarch, btw",
		"body": "We have included nyaofetch to let everyone know that you are using Nyarch Linux, and nyaura to download packages from the Arch User Repository and Arch Linux repositories.",
		"buttons": [
			{
				"label": "Run in terminal",
				"icon": None,
				"style": "suggested-action",
				"command": 'kitty nekofetch'
			}
		]
	},
	{
		"icon": "nyarchscripts-screenshots",
		"icon-size": 400,
		"title": "Check out Nyarch Scripts",
		"body": "Nyarch Scripts offers some interesting and common terminal commands and scripts that can be executed with one click.",
		"buttons": [
			{
				"label": "Run Nyarch Scripts",
				"icon": None,
				"style": "suggested-action",
				"command": 'flatpak run moe.nyarchlinux.scripts'
			}
		]
	},
	{
		"icon": "nyarchupdater-screenshots",
		"icon-size": 400,
		"title": "Keep your system up to date",
		"body": "Nyarch Updater helps you to keep your system up to date and install Nyarch Linux updates.",
		"buttons": [
			{
				"label": "Run Nyarch Updater",
				"icon": None,
				"style": "suggested-action",
				"command": 'flatpak run moe.nyarchlinux.updater'
			}
		]
	},
	{
		"icon": "nyarchassistant-screenshots",
		"icon-size": 400,
		"title": "Your dream waifu at your command",
		"body": "The Nyarch Assistant is a powerful AI assistant that can help you with your system, roleplay and much more thanks to extensions and customizations.",
		"buttons": [
			{
				"label": "Run Nyarch Assistant",
				"icon": None,
				"style": "suggested-action",
				"command": 'flatpak run moe.nyarchlinux.assistant'
			},
		]
    },
    {
		"icon": "timeshift-screenshots",
		"icon-size": 400,
		"title": "Take a Time Leap",
		"body": "With timeshift you can create snapshots (backups) of your system instantly and restore them in milliseconds.",
		"condition": btrfs_fs,
		"buttons": [
			{
				"label": "Open Timeshift",
				"icon": None,
				"style": "suggested-action",
				"command": 'pkexec timeshift-gtk'
			}
		]
	},
	{
		"icon": "online-account-screenshots",
		"icon-size": 400,
		"title": "Stay synced",
		"body": "Add your online accounts in the settings to synchronize calendars, contacts, files and emails.",
		"buttons": [
			{
				"label": "Open Settings",
				"icon": None,
				"style": "suggested-action",
				"command": 'gnome-control-center online-accounts '
			}
		]
	},
	{
		"icon": "gnome-screenshot",
		"icon-size": 400,
		"title": "Discover more about your desktop",
		"body": "Run Gnome Tour to learn more about desktop navigation and touchpad gestures.",
		"buttons": [
			{
				"label": "Start Tour",
				"icon": None,
				"style": "suggested-action",
				"command": 'gnome-tour'
			}
		]
	},
]

