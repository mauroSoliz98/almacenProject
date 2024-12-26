/*
  Warnings:

  - You are about to drop the column `date` on the `departures` table. All the data in the column will be lost.
  - You are about to drop the column `date` on the `entries` table. All the data in the column will be lost.
  - You are about to drop the column `product_name` on the `products` table. All the data in the column will be lost.
  - Added the required column `name` to the `products` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "departures" DROP COLUMN "date",
ADD COLUMN     "create_at" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- AlterTable
ALTER TABLE "entries" DROP COLUMN "date",
ADD COLUMN     "create_at" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- AlterTable
ALTER TABLE "products" DROP COLUMN "product_name",
ADD COLUMN     "name" VARCHAR(50) NOT NULL;
