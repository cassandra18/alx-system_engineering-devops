#!/usr/bin/env ruby
puts ARGV[0].scan(/^[h,b,t,n]{5,8}$/).join
