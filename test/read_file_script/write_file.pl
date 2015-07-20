#! /usr/bin/perl
use strict;
use warnings;

use Path::Class; #library installed via cpan
use autodie; #script dies if problem with read/write

my $dir = dir("/home/b/test");
my $file = $dir->file("team_stats.txt");
my $file_handle = $file->openw();
my @list = ('a', 'list', 'of', 'lines');

foreach my $line ( @list ) {
	#Add the line to the file
	$file_handle->print($line . "\n");
}


