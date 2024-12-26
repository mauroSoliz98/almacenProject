/*
  Warnings:

  - You are about to alter the column `unit_price` on the `departure_product` table. The data in that column could be lost. The data in that column will be cast from `Decimal(10,3)` to `Decimal(10,2)`.
  - You are about to alter the column `unit_price` on the `entry_product` table. The data in that column could be lost. The data in that column will be cast from `Decimal(10,3)` to `Decimal(10,2)`.
  - You are about to alter the column `unit_price` on the `products` table. The data in that column could be lost. The data in that column will be cast from `Decimal(10,3)` to `Decimal(10,2)`.

*/
-- AlterTable
ALTER TABLE "departure_product" ALTER COLUMN "unit_price" SET DATA TYPE DECIMAL(10,2);

-- AlterTable
ALTER TABLE "entry_product" ALTER COLUMN "unit_price" SET DATA TYPE DECIMAL(10,2);

-- AlterTable
ALTER TABLE "products" ALTER COLUMN "unit_price" SET DATA TYPE DECIMAL(10,2);
