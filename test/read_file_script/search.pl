#! /usr/bin/perl
use strict;
use warnings;

use Path::Class;

my $dir = dir('/home','b','test','read_file_script');

#Iterate over the content of
while (my $file = $dir->next) {
	next if $file->is_dir();
	print $file->stringify  . "\n";
}
 
