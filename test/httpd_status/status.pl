#!/usr/bin/perl

use strict;
use warnings;
use LWP::Simple;

my($url)="http://example.com";
my($server_status)=get($url);
my($total_accesses,$total_kbytes,$cpuload,$uptime,$reqpersec,$bytespe
+rsec,$bytesperreq,$busyworkers, $idleworkers,$totalworkers);

if (! $server_status) {
print "Can't access $url\nCheck apache configuration\n\n";
exit(1);
}

$total_accesses = $1 if ($server_status =~ /Total\ Accesses:\ ([\d|\.]
++)/ig)||0;
$total_kbytes = $1 if ($server_status =~ /Total\ kBytes:\ ([\d|\.]+)/g
+i);
$cpuload = $1 if ($server_status =~ /CPULoad:\ ([\d|\.]+)/gi);
$uptime = $1 if ($server_status =~ /Uptime:\ ([\d|\.]+)/gi);
$reqpersec = $1 if ($server_status =~ /ReqPerSec:\ ([\d|\.]+)/gi);
$bytespersec = $1 if ($server_status =~ /BytesPerSec:\ ([\d|\.]+)/gi);
$bytesperreq = $1 if ($server_status =~ /BytesPerReq:\ ([\d|\.]+)/gi);
$busyworkers = $1 if ($server_status =~ /BusyWorkers:\ ([\d|\.]+)/gi);
$idleworkers = $1 if ($server_status =~ /IdleWorkers:\ ([\d|\.]+)/gi);
$totalworkers = $busyworkers + $idleworkers;
#
#printf "TotalAccess %i:Total_kbytes %i:CPU-Load %.2f:reqpersec %.2f:b
+ytespersec %.2f:bytesperreq %.2f:busyworkers %i:idleworkers %i:totalw
+orkers %i\n",$total_accesses,$total_kbytes,$cpuload,$reqpersec,$bytes
+persec,$bytesperreq,$busyworkers,$idleworkers,$totalworkers;
print "busyworkers:$busyworkers bytesperreq:$bytesperreq bytespersec:$
+bytespersec CPULoad:$cpuload idleworkers:$idleworkers reqpersec:$reqp
+ersec TotalAccess:$total_accesses totalworkers:$totalworkers Total_kb
+ytes:$total_kbytes \n";
exit(0);
