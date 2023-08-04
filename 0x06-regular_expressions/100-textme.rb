#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).map { |sender, receiver, flags| "#{sender},#{receiver},#{flags}" }.join(",")
