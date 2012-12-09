django_scavenger
================

django_scavenger is a Django app for building scannable, trackable scavenger hunts. Intended for use by one player (for now!) with a mobile device, django_scavenger allows you to create a set of sequential clues guiding the player along a set path, using QR codes to . As the player reaches each clue, the app will optionally send out an email to a list of recipients you specify, informing them of the player's progress.

How it works
------------

The scavenger hunt is organized so that no one but the intended player can complete the hunt. At each location, the player finds a hidden token, which consists of a QR code and a keyword. They scan the QR code, which takes them to a page within the app that requests a keyword. The player enters the keyword they found at the _previous_ location, and the page displays a written clue pointing them to the next location. To start the scavenger hunt, they must receive the first location and keyword from you (the hunt organizer).

For each stop along the player's path, create a Clue containing the location name (e.g. "Bob's Coffee Shop") and a written clue pointing the player to that location (e.g. "head to the best cafe in town and check the bulletin board"). Link the clues in the order you wish the player to go throughout the scavenger hunt.

Once you've finished writing and organizing the Clues, print out the handy admin sheet for each one. These sheets will contain the token with QR code and keyword, which you then hide in the appropriate location. If you wish to track the player's progress throughout the hunt, enter email addresses into SCAVENGER_SEND_EMAIL.


TODO
----

* This was originally a standalone site. Conversion to Django app is still in progress
* Allow for multiple scavenger hunt participants/team names
* Store email addresses as Users, rather than hardcoding
* Hook into Google Maps for accurate distance/time estimates
* Allow optional hooks into Facebook/Twitter/Instagram
* Write the clue tokens/admin sheets to a single unified PDF, rather than separate pages