puts "Hello World!"

convert = Proc.new { |x| (x.to_f - 32)/1.8}
def cf(c)
    f = (c * 9/5) + 32
    print "#{c} degrees Celcius converted to Fahrenheit is: #{f} degrees."
end

def cfGets()
    print "\n\n---->Please enter a number in degrees Celcius for converting: "
    # gets will place a new line char after the user hits <enter>
    c = gets
    #remove that silly newline char at the end
    c = c.chomp
    #convert user input with a string to a float if possible, else fail
    c = c.to_f
    f = (c * 9/5) + 32

    
    print "#{c} degrees Celcius converted to Fahrenheit is: #{f} degrees."
end

def reverseString()
    print "\n\n---->Please enter a string to reverse: "
    str = gets
    str = str.chomp
    reversedString = ""

    #get the chars of the string into a 'char array'
    chars = str.chars.to_a

    lengthOfString = chars.length - 1

    while lengthOfString >= 0 do
        reversedString += chars[lengthOfString]
        lengthOfString -= 1
    end

    print "\n\nThe original string was #{str}. The new revered string isssss....\n\n\n\n ******** #{reversedString}\n\n\n\n"
end

cf(100)
print "This is the value using a Proc with 1.8: #{convert.call(100)}"

cfGets()

reverseString()
