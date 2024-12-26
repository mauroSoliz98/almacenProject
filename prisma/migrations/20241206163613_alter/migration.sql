/*
  Warnings:

  - You are about to drop the `detail_departures` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `detail_entries` table. If the table is not empty, all the data it contains will be lost.
  - Added the required column `unit_price` to the `products` table without a default value. This is not possible if the table is not empty.
  - Added the required column `units` to the `products` table without a default value. This is not possible if the table is not empty.
  - Made the column `product_name` on table `products` required. This step will fail if there are existing NULL values in that column.
  - Made the column `brand` on table `products` required. This step will fail if there are existing NULL values in that column.

*/
-- DropForeignKey
ALTER TABLE "detail_departures" DROP CONSTRAINT "detail_departures_departures_id_fkey";

-- DropForeignKey
ALTER TABLE "detail_entries" DROP CONSTRAINT "detail_entries_id_entry_fkey";

-- DropForeignKey
ALTER TABLE "detail_entries" DROP CONSTRAINT "detail_entries_id_supplier_fkey";

-- AlterTable
ALTER TABLE "products" ADD COLUMN     "unit_price" DECIMAL(10,3) NOT NULL,
ADD COLUMN     "units" TEXT NOT NULL,
ALTER COLUMN "product_name" SET NOT NULL,
ALTER COLUMN "brand" SET NOT NULL;

-- DropTable
DROP TABLE "detail_departures";

-- DropTable
DROP TABLE "detail_entries";
