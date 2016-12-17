class CreateSeatLines < ActiveRecord::Migration
  def change
    create_table :seat_lines do |t|
      t.integer :line_no
      t.references :seat, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
