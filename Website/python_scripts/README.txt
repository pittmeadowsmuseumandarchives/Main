README
========================================================

This script is designed to modify and add lines quickly
to all the specified html files.

The is based off of a WYSIWYG style config_file, ie 
how the code looks in the config file is how it will
look in your html file.

If it cannot find the line you were looking for it will
not change anything to the file and continue to look
in the other files you specified.

Additional Info:

Copies of the files that you are editing are created by
default and stored in the in the file_copies/ folder.
If anything goes horribly wrong you may always go back
to the old file. Just remember to clean out the
file_copies/ folder everyonce and a while

Dependancies:
	Python 2.7.5
	to check whether python is installed open terminal
	and type "python" and press	enter

HOW TO USE THE SCRIPT:
=========================================================
1) Open the config_file.txt

2) Type the name of the the files you want to modify the
config_file.txt under the heading:

=============== list of HTML Files to change ============
activity.html
archives.html
birthdayparties.html
community.html
contactus.html
curators.html
documents.html
donations.html
exhibits.html
handson.html
heritagetea.html
heritagethursdays.html
history.html
index.html
join.html
library.html
links.html
mapsandplans.html
museumsundays.html
oralhistory.html
ourarchive.html
paranormal.html
photos.html
pittmeadows.html
programs.html
research.html
schooltours.html
studentcoop.html
support.html
template practice.html
template.html
theagm.html
volunteers.html

3) Find the line you wish to modify by copying the entire
line you wish to edit into:

=============== Line to Find ============================
<li><a href="activity.html">Activities</a></li>

4) Replace the line by adding the line under:

=============== Lines To replace ========================
                <li><a href="activity.html">Activities</a>

5) To add multiple lines simply add the additional lines 
under the line you wish to replace
=============== Lines To replace ========================
                <li><a href="activity.html">Activities</a>
                    <ul>
                    <li><a href="handson.html">Hands On</a></li>
                    <li><a href="activity.html">Activity Sheets</a></li>
                    <li><a href="discoveryboxes">Discovery Boxes</a></li>
                    </ul>
                </li>
==========================================================

6) Double click the multi_file_text_edit.py file to 
execute the code. If that doesn't work cd to 
multi_file_text_edit.py and type:

    python multi_file_text_edit.py

you should see terminal or command prompt startup 
and show that the file has appended your text.


Deleting Lines:
==========================================================

1) Search for the line before the line you wish to delete.

=============== Line to Find ============================
<li><a href="activity.html">Activities</a>

2) Then under lines to replace just type "delete_line" to 
delete a line:

=============== Lines To replace ========================
                <li><a href="activity.html">Activities</a></li>
delete_line                    <ul>
delete_line                    <li><a href="handson.html">Hands On</a></li>
delete_line                    <li><a href="activity.html">Activity Sheets</a></li>
delete_line                    <li><a href="discoveryboxes">Discovery Boxes</a></li>
delete_line                    </ul>
delete_line                </li>
==========================================================

NOTE that it doesn't matter if there is a html code after
it or not and you would obtain the same result by doing:

=============== Lines To replace ========================
                <li><a href="activity.html">Activities</a></li>
delete_line
delete_line
delete_line
delete_line
delete_line
delete_line
=========================================================




