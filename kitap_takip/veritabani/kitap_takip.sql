PGDMP                      }            kitap_takip    17.2    17.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16397    kitap_takip    DATABASE     �   CREATE DATABASE kitap_takip WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE kitap_takip;
                     postgres    false            �            1259    16409 	   kullanici    TABLE     �   CREATE TABLE public.kullanici (
    k_kullaniciadi character varying(20) NOT NULL,
    k_sifre character varying(6) NOT NULL,
    k_kitap_ad character varying(40),
    k_kitap_toplam_sayfa integer,
    k_okunan_sayfa integer DEFAULT 0
);
    DROP TABLE public.kullanici;
       public         heap r       postgres    false                      0    16409 	   kullanici 
   TABLE DATA           n   COPY public.kullanici (k_kullaniciadi, k_sifre, k_kitap_ad, k_kitap_toplam_sayfa, k_okunan_sayfa) FROM stdin;
    public               postgres    false    217   B       �           2606    16413    kullanici kullanici_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.kullanici
    ADD CONSTRAINT kullanici_pkey PRIMARY KEY (k_kullaniciadi);
 B   ALTER TABLE ONLY public.kullanici DROP CONSTRAINT kullanici_pkey;
       public                 postgres    false    217               p   x��H���/�/�I�442615�4B��Բ����ԢԂ��_b�9
���ޓwxO���s�&f䖖pf'%r��%�p�倘�85'3��2ђ3���b���� F$"     