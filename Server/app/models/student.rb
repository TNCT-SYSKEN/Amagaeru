class Student < ActiveRecord::Base
  def getDepertment
    depertment
  end

  def getGrade
    grade
  end

  def setGrade(grade)
    self.grade = grade
  end

  def incrementGrade
    self.grade += self.grade
  end

  def getNumber
    number
  end

  def setNumber(number)
    self.number = number
  end

  def getName
    first_name + last_name
  end
end
