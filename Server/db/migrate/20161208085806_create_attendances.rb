class CreateAttendances < ActiveRecord::Migration
  def change
    create_table :attendances do |t|
      t.string :department
      t.integer :grade

      t.timestamps null: false
    end
  end
end
