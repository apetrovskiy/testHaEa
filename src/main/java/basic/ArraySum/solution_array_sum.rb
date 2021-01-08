=begin
# Sample code to perform I/O:

name = gets.chomp                # Reading input from STDIN
print "Hi, #{name}.\n"           # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
=end

# Write your code here
def solution_array_sum(input_array)
    input_array.inject(0, :+)
end

=begin
array_length = gets.chomp
array = gets.split(" ").map(&:to_i)
puts solution_array_sum(array)
=end
