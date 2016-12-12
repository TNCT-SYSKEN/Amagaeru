class SeatLine < ActiveRecord::Base
  belongs_to :seat
  has_many :seat_data
end
