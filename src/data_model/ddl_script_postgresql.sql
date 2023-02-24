-- DDL (Data definition language) for database and tables creation for PostgreSQL

-- create database
CREATE  DATABASE live_traffic_cameras;


-- create a schema inside the database
CREATE SCHEMA live_traffic_cameras;

-- create tables

CREATE table live_traffic_cameras.d_camera_trafikoa (
    id INTEGER NOT NULL,
    url_image VARCHAR,
    road VARCHAR,
    km FLOAT8,
    location_info VARCHAR,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE table live_traffic_cameras.d_camera_andorra (
    id INTEGER NOT NULL,
    url_image VARCHAR,
    road VARCHAR,
    km FLOAT8,
    location_info VARCHAR,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE table live_traffic_cameras.d_camera_dgt (
    id INTEGER NOT NULL,
    url_image VARCHAR,
    road VARCHAR,
    km FLOAT8,
    location_info VARCHAR,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE live_traffic_cameras.d_update_history_dgt (
    id SERIAL,
    camera_id INTEGER NOT NULL,
    url_image VARCHAR,
    road VARCHAR,
    km FLOAT8,
    location_info VARCHAR,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);


CREATE TABLE live_traffic_cameras.d_update_history_trafikoa (
    id SERIAL,
    camera_id INTEGER NOT NULL,
    url_image VARCHAR,
    road VARCHAR,
    km FLOAT8,
    location_info VARCHAR,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);


CREATE TABLE live_traffic_cameras.d_update_history_andorra (
    id SERIAL,
    camera_id INTEGER NOT NULL,
    url_image VARCHAR,
    road VARCHAR,
    km FLOAT8,
    location_info VARCHAR,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);