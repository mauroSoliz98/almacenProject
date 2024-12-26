/*
  Warnings:

  - You are about to drop the `Departure` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Detail_departure` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Detail_entry` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Entry` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Product` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Supplier` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Detail_departure" DROP CONSTRAINT "Detail_departure_departures_id_fkey";

-- DropForeignKey
ALTER TABLE "Detail_entry" DROP CONSTRAINT "Detail_entry_id_entry_fkey";

-- DropForeignKey
ALTER TABLE "Detail_entry" DROP CONSTRAINT "Detail_entry_id_supplier_fkey";

-- DropForeignKey
ALTER TABLE "departure_product" DROP CONSTRAINT "departures_products_id_departure_fkey";

-- DropForeignKey
ALTER TABLE "departure_product" DROP CONSTRAINT "departures_products_id_product_fkey";

-- DropForeignKey
ALTER TABLE "entry_product" DROP CONSTRAINT "entries_products_id_entry_fkey";

-- DropForeignKey
ALTER TABLE "entry_product" DROP CONSTRAINT "entries_products_id_product_fkey";

-- DropTable
DROP TABLE "Departure";

-- DropTable
DROP TABLE "Detail_departure";

-- DropTable
DROP TABLE "Detail_entry";

-- DropTable
DROP TABLE "Entry";

-- DropTable
DROP TABLE "Product";

-- DropTable
DROP TABLE "Supplier";

-- CreateTable
CREATE TABLE "departures" (
    "id" SERIAL NOT NULL,
    "unit_price" DECIMAL(10,3),
    "total_price" DECIMAL(10,3),
    "quantity" INTEGER,
    "unit" VARCHAR(50),

    CONSTRAINT "departures_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "detail_departures" (
    "id" BIGSERIAL NOT NULL,
    "departures_id" INTEGER,
    "date_departure" TIMESTAMPTZ(6),
    "destiny" TEXT,

    CONSTRAINT "detail_departures_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "detail_entries" (
    "id" BIGSERIAL NOT NULL,
    "id_entry" BIGINT,
    "receptionist" TEXT,
    "date_enty" TIMESTAMPTZ(6),
    "id_supplier" BIGINT,

    CONSTRAINT "detail_entries_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "entries" (
    "id" BIGSERIAL NOT NULL,
    "units" TEXT,
    "unit_price" DECIMAL(10,2),
    "total" DECIMAL(10,2),

    CONSTRAINT "entries_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "products" (
    "id" SERIAL NOT NULL,
    "product_name" VARCHAR(50),
    "brand" VARCHAR(50),
    "description" TEXT,

    CONSTRAINT "pruducts_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "suppliers" (
    "id" BIGSERIAL NOT NULL,
    "supplier_name" VARCHAR(50),
    "phone_number" INTEGER,
    "mail" TEXT,
    "location" TEXT,

    CONSTRAINT "supplier_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "departure_product" ADD CONSTRAINT "departures_products_id_departure_fkey" FOREIGN KEY ("id_departure") REFERENCES "departures"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "departure_product" ADD CONSTRAINT "departures_products_id_product_fkey" FOREIGN KEY ("id_product") REFERENCES "products"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "detail_departures" ADD CONSTRAINT "detail_departures_departures_id_fkey" FOREIGN KEY ("departures_id") REFERENCES "departures"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "detail_entries" ADD CONSTRAINT "detail_entries_id_entry_fkey" FOREIGN KEY ("id_entry") REFERENCES "entries"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "detail_entries" ADD CONSTRAINT "detail_entries_id_supplier_fkey" FOREIGN KEY ("id_supplier") REFERENCES "suppliers"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "entry_product" ADD CONSTRAINT "entry_product_id_entry_fkey" FOREIGN KEY ("id_entry") REFERENCES "entries"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "entry_product" ADD CONSTRAINT "entry_product_id_product_fkey" FOREIGN KEY ("id_product") REFERENCES "products"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
