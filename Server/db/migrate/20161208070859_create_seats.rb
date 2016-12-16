class CreateSeats < ActiveRecord::Migration
  def change
    create_table :seats do |t|
      t.string :depertment
      t.integer :gread

      t.timestamps null: false
    end
  end
end
