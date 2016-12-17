class RenameDateColumnToTests < ActiveRecord::Migration
  def change
    rename_column :seats, :gread, :grade
  end
end
