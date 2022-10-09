Norn Statistics (1.2)

This agent adds a panel to the left of the screen that displays various
information about your creatures, including their age, life stage,
generation, and if they have been through the warp.  The information
is updated about every 15 seconds.

It also checks for possible immortal and fast-aging creatures by
checking 3 indicators:

1. Creatures older than 9 hours may be immortal.
2. Creatures with 2 or more toxins in their body over 95 may be
   immortal.
3. Creatures that reached adult stage before a certain age are
   probably fast-agers.

If any of these checks are matched then a "boing" sound will be heard
and 1 or more letters will appear in square brackets along with the
rest of the information for that creature:

O = Old
T = Toxins (not checked for Grendels)
A = Aging

This checking can be turned on or off with the O/T/A button.

The top four buttons are used to toggle on or off the display of the
various species and the two arrow buttons are used to scroll the
window if there is more than one page of text.

The text at the bottom of the panel show the number of male, number of
female and highest generation of each species.

Installation
------------
If you are upgrading from version 1.1 or earlier then you should
manually copy the included "norn stats.catalogue" file into your
"Catalogue" folder.  This updates the agent help within the game
as this file will not be automatically updated if it already exists.

If this is the first version you have used then you can ignore the
"norn stats.catalogue" file.

Thanks
------
Thanks to Random (http://members.home.net/dockingstation/) for the
suggestion for this agent.

Version history
---------------
1.2
- The display now updates straight away when injected, rather than
  waiting for the first timed check.
- Added fast ager/immortal checking.  This can be toggled on and off.
- Added support for Ettins, Grendels and Geats.  The display of any of
  these (as well as Norns) can be toggled on and off individually.
- Added counters to the bottom of the panel.  These count the number
  of male and female of each species as well as showing the highest
  generation.
- The agent can now be injected using the C3 creator machine without
  causing errors (or killing the machine if auto-kill is enabled).
1.1
- The "youth" stage was missed out of the life stages, so stages after
  "adolescent" would incorrectly report as one greater than they
  actually were.

Emmental
http://creatures.webhop.net
