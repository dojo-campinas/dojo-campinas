class PhoneExpression
  attr_reader :expression
  
  @@translate_map = {
    "A" => "2", "B" => "2", "C" => "2",
    "D" => "3", "E" => "3", "F" => "3",
    "G" => "4", "H" => "4", "I" => "4",
    "-" => "-", "0" => "0", "1" => "1",
  }
  
  def initialize(expression)
    @expression = expression
  end
  
  def phone
    mod_exp = ""    
    @expression.each_char do |e|
      mod_exp << @@translate_map[e] 
    end
    mod_exp
  end
  
end
