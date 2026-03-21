CREATE OR ALTER PROCEDURE LoadDataToBronze AS
BEGIN
	DECLARE @start_time DATETIME, @end_time DATETIME, @batch_start_time DATETIME, @batch_end_time DATETIME;

	SET @batch_start_time = GETDATE();
	PRINT '================================================';
	PRINT 'Loading Bronze Layer';
	PRINT '================================================';

	-- Loading bronze.crm_cust_info
	SET @start_time = GETDATE();
	PRINT '>> Truncating Table: bronze.crm_cust_info';
	TRUNCATE TABLE bronze.crm_cust_info;
	PRINT '>> Inserting Data Into: bronze.crm_cust_info';
	BULK INSERT bronze.crm_cust_info
	FROM 'D:\Sama\studying\Data warehouse\Data Warehouse-Medallion Architecture Project\datasets\source_crm\cust_info.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
	SET @end_time = GETDATE();
	PRINT '>> Load Duration: ' + CAST(DATEDIFF(SECOND, @start_time, @end_time) AS NVARCHAR) + ' seconds';
	PRINT '>> -------------';

	-- Loading bronze.crm_prd_info
	SET @start_time = GETDATE();
	PRINT '>> Truncating Table: bronze.crm_prd_info';
	TRUNCATE TABLE bronze.crm_prd_info;
	PRINT '>> Inserting Data Into: bronze.crm_prd_info';
	BULK INSERT bronze.crm_prd_info
	FROM 'D:\Sama\studying\Data warehouse\Data Warehouse-Medallion Architecture Project\datasets\source_crm\prd_info.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
	SET @end_time = GETDATE();
	PRINT '>> Load Duration: ' + CAST(DATEDIFF(SECOND, @start_time, @end_time) AS NVARCHAR) + ' seconds';
	PRINT '>> -------------';

	-- Loading bronze.crm_sales_details
	SET @start_time = GETDATE();
	PRINT '>> Truncating Table: bronze.crm_sales_details';
	TRUNCATE TABLE bronze.crm_sales_details;
	PRINT '>> Inserting Data Into: bronze.crm_sales_details';
	BULK INSERT bronze.crm_sales_details
	FROM 'D:\Sama\studying\Data warehouse\Data Warehouse-Medallion Architecture Project\datasets\source_crm\sales_details.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
	SET @end_time = GETDATE();
	PRINT '>> Load Duration: ' + CAST(DATEDIFF(SECOND, @start_time, @end_time) AS NVARCHAR) + ' seconds';
	PRINT '>> -------------';

	-- Loading bronze.erp_cust_az12
	SET @start_time = GETDATE();
	PRINT '>> Truncating Table: bronze.erp_cust_az12';
	TRUNCATE TABLE bronze.erp_cust_az12;
	PRINT '>> Inserting Data Into: bronze.erp_cust_az12';
	BULK INSERT bronze.erp_cust_az12
	FROM 'D:\Sama\studying\Data warehouse\Data Warehouse-Medallion Architecture Project\datasets\source_erp\CUST_AZ12.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
	SET @end_time = GETDATE();
	PRINT '>> Load Duration: ' + CAST(DATEDIFF(SECOND, @start_time, @end_time) AS NVARCHAR) + ' seconds';
	PRINT '>> -------------';

	-- Loading bronze.erp_loc_a101
	SET @start_time = GETDATE();
	PRINT '>> Truncating Table: bronze.erp_loc_a101';
	TRUNCATE TABLE bronze.erp_loc_a101;
	PRINT '>> Inserting Data Into: bronze.erp_loc_a101';
	BULK INSERT bronze.erp_loc_a101
	FROM 'D:\Sama\studying\Data warehouse\Data Warehouse-Medallion Architecture Project\datasets\source_erp\LOC_A101.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
	SET @end_time = GETDATE();
	PRINT '>> Load Duration: ' + CAST(DATEDIFF(SECOND, @start_time, @end_time) AS NVARCHAR) + ' seconds';
	PRINT '>> -------------';

	-- Loading bronze.erp_px_cat_g1v2
	SET @start_time = GETDATE();
	PRINT '>> Truncating Table: bronze.erp_px_cat_g1v2';
	TRUNCATE TABLE bronze.erp_px_cat_g1v2;
	PRINT '>> Inserting Data Into: bronze.erp_px_cat_g1v2';
	BULK INSERT bronze.erp_px_cat_g1v2
	FROM 'D:\Sama\studying\Data warehouse\Data Warehouse-Medallion Architecture Project\datasets\source_erp\PX_CAT_G1V2.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
	SET @end_time = GETDATE();
	PRINT '>> Load Duration: ' + CAST(DATEDIFF(SECOND, @start_time, @end_time) AS NVARCHAR) + ' seconds';
	PRINT '>> -------------';

	SET @batch_end_time = GETDATE();
	PRINT '=========================================='
	PRINT 'Loading Bronze Layer is Completed';
	PRINT '   - Total Load Duration: ' + CAST(DATEDIFF(SECOND, @batch_start_time, @batch_end_time) AS NVARCHAR) + ' seconds';
	PRINT '=========================================='
END



SELECT 'bronze.crm_cust_info' AS table_name, COUNT(*) AS row_count FROM bronze.crm_cust_info
UNION ALL
SELECT 'bronze.crm_prd_info', COUNT(*) FROM bronze.crm_prd_info
UNION ALL
SELECT 'bronze.crm_sales_details', COUNT(*) FROM bronze.crm_sales_details
UNION ALL
SELECT 'bronze.erp_cust_az12', COUNT(*) FROM bronze.erp_cust_az12
UNION ALL
SELECT 'bronze.erp_loc_a101', COUNT(*) FROM bronze.erp_loc_a101
UNION ALL
SELECT 'bronze.erp_px_cat_g1v2', COUNT(*) FROM bronze.erp_px_cat_g1v2;
