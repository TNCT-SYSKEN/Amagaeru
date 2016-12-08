class CreateSeatData < ActiveRecord::Migration
  def change
    create_table :seat_data do |t|
      t.integer :number
      t.string :first_name
      t.string :last_name
      t.references :seat_line, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
