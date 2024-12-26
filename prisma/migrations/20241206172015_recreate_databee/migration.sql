/*
  Warnings:

  - The primary key for the `departure_product` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - You are about to drop the column `quantity` on the `departures` table. All the data in the column will be lost.
  - You are about to drop the column `total_price` on the `departures` table. All the data in the column will be lost.
  - You are about to drop the column `unit` on the `departures` table. All the data in the column will be lost.
  - You are about to drop the column `unit_price` on the `departures` table. All the data in the column will be lost.
  - You are about to drop the column `total` on the `entries` table. All the data in the column will be lost.
  - You are about to drop the column `unit_price` on the `entries` table. All the data in the column will be lost.
  - You are about to drop the column `units` on the `entries` table. All the data in the column will be lost.
  - The primary key for the `entry_product` table will be changed. If it partially fails, the table could be left without primary key constraint.
  - Added the required column `order` to the `departure_product` table without a default value. This is not possible if the table is not empty.
  - Added the required column `quantity` to the `departure_product` table without a default value. This is not possible if the table is not empty.
  - Added the required column `date` to the `departures` table without a default value. This is not possible if the table is not empty.
  - Added the required column `destiny` to the `departures` table without a default value. This is not possible if the table is not empty.
  - Added the required column `date` to the `entries` table without a default value. This is not possible if the table is not empty.
  - Added the required column `id_supplier` to the `entries` table without a default value. This is not possible if the table is not empty.
  - Added the required column `order` to the `entry_product` table without a default value. This is not possible if the table is not empty.
  - Added the required column `quantity` to the `entry_product` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE "departure_product" DROP CONSTRAINT "departures_products_id_departure_fkey";

-- DropForeignKey
ALTER TABLE "departure_product" DROP CONSTRAINT "departures_products_id_product_fkey";

-- AlterTable
ALTER TABLE "departure_product" DROP CONSTRAINT "departure_product_pkey",
ADD COLUMN     "order" INTEGER NOT NULL,
ADD COLUMN     "quantity" INTEGER NOT NULL,
ADD CONSTRAINT "departure_product_pkey" PRIMARY KEY ("id_departure", "order");

-- AlterTable
ALTER TABLE "departures" DROP COLUMN "quantity",
DROP COLUMN "total_price",
DROP COLUMN "unit",
DROP COLUMN "unit_price",
ADD COLUMN     "date" TIMESTAMP(6) NOT NULL,
ADD COLUMN     "destiny" TEXT NOT NULL;

-- AlterTable
ALTER TABLE "entries" DROP COLUMN "total",
DROP COLUMN "unit_price",
DROP COLUMN "units",
ADD COLUMN     "date" TIMESTAMP(6) NOT NULL,
ADD COLUMN     "id_supplier" BIGINT NOT NULL;

-- AlterTable
ALTER TABLE "entry_product" DROP CONSTRAINT "entry_product_pkey",
ADD COLUMN     "order" INTEGER NOT NULL,
ADD COLUMN     "quantity" INTEGER NOT NULL,
ADD CONSTRAINT "entry_product_pkey" PRIMARY KEY ("id_entry", "order");

-- AddForeignKey
ALTER TABLE "departure_product" ADD CONSTRAINT "departure_product_id_departure_fkey" FOREIGN KEY ("id_departure") REFERENCES "departures"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "departure_product" ADD CONSTRAINT "departure_product_id_product_fkey" FOREIGN KEY ("id_product") REFERENCES "products"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "entries" ADD CONSTRAINT "entries_id_supplier_fkey" FOREIGN KEY ("id_supplier") REFERENCES "suppliers"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
