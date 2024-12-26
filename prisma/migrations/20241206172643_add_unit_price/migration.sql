/*
  Warnings:

  - Added the required column `unit_price` to the `departure_product` table without a default value. This is not possible if the table is not empty.
  - Added the required column `unit_price` to the `entry_product` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "departure_product" ADD COLUMN     "unit_price" DECIMAL(10,3) NOT NULL;

-- AlterTable
ALTER TABLE "entry_product" ADD COLUMN     "unit_price" DECIMAL(10,3) NOT NULL;
