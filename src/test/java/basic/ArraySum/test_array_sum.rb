require 'rspec'
require 'rspec/autorun'
# require 'rubygems'
# require 'minitest/autorun'
require_relative '../../../../main/java/basic/ArraySum/solution_array_sum'

RSpec.describe 'array sum' do
# describe 'array sum' do
  describe 'array sum method' do
    subject { solution_array_sum input }

    [
      [[1_000_000_001, 1_000_000_002, 1_000_000_003, 1_000_000_004, 1_000_000_005], 5_000_000_015],
      [[1_001_458_909, 1_004_570_889, 1_007_019_111, 1_003_302_837, 1_002_514_638, 1_006_431_461, 1_002_575_010, 1_007_514_041, 1_007_548_981, 1_004_402_249], 10_047_338_126]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        actual_result = solution_array_sum(input)
        expect(actual_result).to be == expected_output
        expect(solution_array_sum(input)).to eql expected_output
      end
    end
  end
end

=begin
class ArraySumTests < MiniTest::Unit::TestCase
  [
    [[1_000_000_001, 1_000_000_002, 1_000_000_003, 1_000_000_004, 1_000_000_005], 5_000_000_015],
    [[1_001_458_909, 1_004_570_889, 1_007_019_111, 1_003_302_837, 1_002_514_638, 1_006_431_461, 1_002_575_010, 1_007_514_041, 1_007_548_981, 1_004_402_249], 10_047_338_126]
  ].each do |input, expected_output|
    define_method("test_output_is_#{expected_output}") do
      assert_equal(expected_output, solution_array_sum(input))
    end
  end
end
=end
