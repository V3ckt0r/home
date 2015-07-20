#!/usr/bin/perl
use strict;
use warnings;
use Path::Class;
use autodie; #die if problems reading

my $count = 0;

my $dir = dir("/home/b/test");

my $file = $dir->file("team_stats.txt");

#read contents of file
my $content = $file->slurp();

#openr() returns an IO::File ojbect to read from
my $file_handle = $file->openr();

#Read in line at a time
while( my $line = $file_handle->getline() ) {
	print $line;
	if ($line = "line") {
		$count++;
	} 
}
print "$count\n";
