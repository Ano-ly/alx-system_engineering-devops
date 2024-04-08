#!/usr/bin/env ruby
s = ARGV[0].scan(/\[from:([^\]]+)\]\s\[to:[^\]]+\]\s\[flags:[^\]]+\]/).join
r = ARGV[0].scan(/\[from:[^\]]+\]\s\[to:([^\]]+)\]\s\[flags:[^\]]+\]/).join
f = ARGV[0].scan(/\[from:[^\]]+\]\s\[to:[^\]]+\]\s\[flags:([^\]]+)\]/).join
puts "#{s},#{r},#{f}"
