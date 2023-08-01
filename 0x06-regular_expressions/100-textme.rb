#!/usr/bin/env ruby
puts ARGV[0].scan(//SENDER_REGEX|RECEIVER_REGEX|FLAGS_REGEX/).join(',')
