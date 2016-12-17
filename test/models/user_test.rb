require 'test_helper'

class UserTest < ActiveSupport::TestCase
  def setup
    @ser = User.new(name: "Example User", authority: TRUE,password: "foobar", password_confirmation: "foobar")
  end
  

end
