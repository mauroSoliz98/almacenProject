-- CreateTable
CREATE TABLE "departure_product" (
    "id_departure" INTEGER NOT NULL,
    "id_product" INTEGER NOT NULL,

    CONSTRAINT "departure_product_pkey" PRIMARY KEY ("id_departure","id_product")
);

-- CreateTable
CREATE TABLE "Departure" (
    "id" SERIAL NOT NULL,
    "unit_price" DECIMAL(10,3),
    "total_price" DECIMAL(10,3),
    "quantity" INTEGER,
    "unit" VARCHAR(50),

    CONSTRAINT "Departure_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Detail_departure" (
    "id" BIGSERIAL NOT NULL,
    "departures_id" INTEGER,
    "date_departure" TIMESTAMPTZ(6),
    "destiny" TEXT,

    CONSTRAINT "Detail_departure_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Detail_entry" (
    "id" BIGSERIAL NOT NULL,
    "id_entry" BIGINT,
    "receptionist" TEXT,
    "date_enty" TIMESTAMPTZ(6),
    "id_supplier" BIGINT,

    CONSTRAINT "Detail_entry_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Entry" (
    "id" BIGSERIAL NOT NULL,
    "units" TEXT,
    "unit_price" DECIMAL(10,2),
    "total" DECIMAL(10,2),

    CONSTRAINT "Entry_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "entry_product" (
    "id_entry" BIGINT NOT NULL,
    "id_product" INTEGER NOT NULL,

    CONSTRAINT "entry_product_pkey" PRIMARY KEY ("id_entry","id_product")
);

-- CreateTable
CREATE TABLE "Product" (
    "id" SERIAL NOT NULL,
    "product_name" VARCHAR(50),
    "brand" VARCHAR(50),
    "description" TEXT,

    CONSTRAINT "pruducts_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Supplier" (
    "id" BIGSERIAL NOT NULL,
    "supplier_name" VARCHAR(50),
    "phone_number" INTEGER,
    "mail" TEXT,
    "location" TEXT,

    CONSTRAINT "supplier_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "departure_product" ADD CONSTRAINT "departures_products_id_departure_fkey" FOREIGN KEY ("id_departure") REFERENCES "Departure"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "departure_product" ADD CONSTRAINT "departures_products_id_product_fkey" FOREIGN KEY ("id_product") REFERENCES "Product"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "Detail_departure" ADD CONSTRAINT "Detail_departure_departures_id_fkey" FOREIGN KEY ("departures_id") REFERENCES "Departure"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "Detail_entry" ADD CONSTRAINT "Detail_entry_id_entry_fkey" FOREIGN KEY ("id_entry") REFERENCES "Entry"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "Detail_entry" ADD CONSTRAINT "Detail_entry_id_supplier_fkey" FOREIGN KEY ("id_supplier") REFERENCES "Supplier"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "entry_product" ADD CONSTRAINT "entries_products_id_entry_fkey" FOREIGN KEY ("id_entry") REFERENCES "Entry"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "entry_product" ADD CONSTRAINT "entries_products_id_product_fkey" FOREIGN KEY ("id_product") REFERENCES "Product"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

