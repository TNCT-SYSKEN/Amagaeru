class Timetable < ActiveRecord::Base
  has_many :day_timetables
end
