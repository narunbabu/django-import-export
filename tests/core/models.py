from __future__ import unicode_literals
import random
import string

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField( max_length=100)
    birthday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Book(models.Model):
    name = models.CharField( 'Book name', max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    published_time = models.TimeField('Time published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Parent(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Child(models.Model):
    parent = models.ForeignKey(Parent)
    name = models.CharField( max_length=100)

    def __str__(self):
        return '%s - child of %s' % (self.name, self.parent.name)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    is_private = models.BooleanField(default=True)


class Entry(models.Model):
    user = models.ForeignKey('auth.User')


class WithDefault(models.Model):
    name = models.CharField('Default', max_length=75, blank=True,
                            default='foo_bar')

def random_name():
    chars = string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(chars) for _ in range(100))

class WithDynamicDefault(models.Model):

    name = models.CharField( 'Dyn Default', max_length=100,
            default=random_name)


class WithFloatField(models.Model):
    f = models.FloatField(blank=True, null=True)

@python_2_unicode_compatible
class Census(models.Model):
    state_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    dist_code = models.IntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    sub_dist_name = models.IntegerField(blank=True, null=True)
    sub_dist_code = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    vil_code = models.IntegerField(blank=True, null=True)
    vil_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    cdb_code = models.IntegerField(blank=True, null=True)
    cdb_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    gram_pan_code = models.IntegerField(blank=True, null=True)
    gram_pan_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ref_year = models.IntegerField(blank=True, null=True)
    sub_dist_hquarter_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    sub_dist_hquarter_distance = models.IntegerField(blank=True, null=True)
    dist_hquarter_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    dist_hquarter_dist = models.IntegerField(blank=True, null=True)
    nearest_stat_town_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    nearest_stat_town_dist = models.IntegerField(blank=True, null=True)
    within_state_ut_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    within_state_ut_dist = models.IntegerField(blank=True, null=True)
    outside_state_ut_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    outside_state_ut_dist = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    tot_geograph_area = models.IntegerField(blank=True, null=True)
    tot_households = models.IntegerField(blank=True, null=True)
    tot_population = models.IntegerField(blank=True, null=True)
    tot_male_population = models.IntegerField(blank=True, null=True)
    tot_female_population = models.IntegerField(blank=True, null=True)
    tot_sc_population = models.IntegerField(blank=True, null=True)
    tot_scm_population = models.IntegerField(blank=True, null=True)
    tot_scf_population = models.IntegerField(blank=True, null=True)
    tot_st_population = models.IntegerField(blank=True, null=True)
    tot_stm_population = models.IntegerField(blank=True, null=True)
    tot_stf_population = models.IntegerField(blank=True, null=True)
    gov_preprim_sch_status = models.IntegerField(blank=True, null=True)
    gov_preprim_sch_nos = models.IntegerField(blank=True, null=True)
    pvt_preprim_sch_status = models.IntegerField(blank=True, null=True)
    pvt_preprim_sch_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_preprim = models.IntegerField(blank=True, null=True)
    nfaci_village_town_preprim = models.CharField(max_length=30, blank=True, null=True)
    ina_distcode_preprim = models.CharField(max_length=2, blank=True, null=True)
    gov_prim_sch_status = models.IntegerField(blank=True, null=True)
    gov_prim_sch_nos = models.IntegerField(blank=True, null=True)
    pvt_prim_sch_status = models.IntegerField(blank=True, null=True)
    pvt_prim_sch_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_prim = models.IntegerField(blank=True, null=True)
    nfaci_village_town_prim = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_prim = models.CharField(max_length=2, blank=True, null=True)
    gov_mid_sch_status = models.NullBooleanField()
    gov_mid_sch_nos = models.IntegerField(blank=True, null=True)
    pvt_mid_sch_status = models.NullBooleanField()
    pvt_mid_sch_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_mid = models.NullBooleanField()
    nfaci_village_town_mid = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_mid = models.CharField(max_length=2, blank=True, null=True)
    gov_sec_sch_status = models.NullBooleanField()
    gov_sec_sch_nos = models.IntegerField(blank=True, null=True)
    pvt_sec_sch_status = models.NullBooleanField()
    pvt_sec_sch_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_sec = models.NullBooleanField()
    nfaci_village_town_sec = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_sec = models.CharField(max_length=2, blank=True, null=True)
    gov_sen_sec_sch_status = models.NullBooleanField()
    gov_sen_sec_sch_nos = models.IntegerField(blank=True, null=True)
    pvt_sen_sec_sch_status = models.NullBooleanField()
    pvt_sen_sec_sch_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_sen_sec = models.NullBooleanField()
    nfaci_village_town_sen_sec = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_sen_sec = models.CharField(max_length=2, blank=True, null=True)
    gov_deg_col_status = models.NullBooleanField()
    gov_deg_col_nos = models.IntegerField(blank=True, null=True)
    pvt_deg_col_status = models.NullBooleanField()
    pvt_deg_col_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_deg_col = models.NullBooleanField()
    nfaci_village_town_deg_col = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_deg_col = models.CharField(max_length=2, blank=True, null=True)
    gov_eng_col_status = models.NullBooleanField()
    gov_eng_col_nos = models.IntegerField(blank=True, null=True)
    pvt_eng_col_status = models.NullBooleanField()
    pvt_eng_col_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_eng_col = models.NullBooleanField()
    nfaci_village_town_eng_col = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_eng_col = models.CharField(max_length=2, blank=True, null=True)
    gov_med_col_status = models.NullBooleanField()
    gov_med_col_nos = models.IntegerField(blank=True, null=True)
    pvt_med_col_status = models.NullBooleanField()
    pvt_med_col_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_med_col = models.NullBooleanField()
    nfaci_village_town_med_col = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_med_col = models.CharField(max_length=2, blank=True, null=True)
    gov_mgmt_inst_status = models.NullBooleanField()
    gov_mgmt_inst_nos = models.IntegerField(blank=True, null=True)
    pvt_mgmt_inst_status = models.NullBooleanField()
    pvt_mgmt_inst_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_mgmt_inst = models.NullBooleanField()
    nfaci_village_town_mgmt_inst = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_mgmt_inst = models.CharField(max_length=2, blank=True, null=True)
    gov_polytech_status = models.NullBooleanField()
    gov_polytech_nos = models.IntegerField(blank=True, null=True)
    pvt_polytech_status = models.NullBooleanField()
    pvt_polytech_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_polytech = models.NullBooleanField()
    nfaci_village_town_polytech = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_polytech = models.CharField(max_length=2, blank=True, null=True)
    gov_voc_training_status = models.NullBooleanField()
    gov_voc_training_nos = models.IntegerField(blank=True, null=True)
    pvt_voc_training_status = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    pvt_voc_training_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_voc_training = models.NullBooleanField()
    nfaci_village_town_voc_training = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_voc_training = models.CharField(max_length=2, blank=True, null=True)
    gov_nonformal_training_status = models.NullBooleanField()
    gov_nonformal_training_nos = models.IntegerField(blank=True, null=True)
    pvt_nonformal_training_status = models.NullBooleanField()
    pvt_nonformal_training_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_nonformal_training = models.NullBooleanField()
    nfaci_village_town_nonformal_training = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_nonformal_training = models.CharField(max_length=2, blank=True, null=True)
    gov_sch_for_dasabled_status = models.NullBooleanField()
    gov_sch_for_dasabled_nos = models.IntegerField(blank=True, null=True)
    pvt_sch_for_dasabled_status = models.NullBooleanField()
    pvt_sch_for_dasabled_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_sch_for_dasabled = models.NullBooleanField()
    nfaci_village_town_sch_for_dasabled = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_sch_for_dasabled = models.CharField(max_length=2, blank=True, null=True)
    gov_others_status = models.NullBooleanField()
    gov_others_nos = models.IntegerField(blank=True, null=True)
    pri_others_status = models.NullBooleanField()
    pri_others_nos = models.IntegerField(blank=True, null=True)
    nfaci_status_others = models.NullBooleanField()
    nfaci_village_town_others = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    ina_distcode_others = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'census'

class CensusRest(models.Model):
    vil_code = models.IntegerField(blank=True, null=True)
    com_health_centre_nos = models.IntegerField(blank=True, null=True)
    com_health_centre_doct_tot_nos = models.IntegerField(blank=True, null=True)
    com_health_centre_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    com_health_centre_staff_tot_nos = models.IntegerField(blank=True, null=True)
    com_health_centre_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_com_health_centre = models.CharField(max_length=2, blank=True, null=True)
    prim_health_centre_nos = models.IntegerField(blank=True, null=True)
    prim_health_centre_doct_tot_nos = models.IntegerField(blank=True, null=True)
    prim_health_centre_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    prim_health_centre_staff_tot_nos = models.IntegerField(blank=True, null=True)
    prim_health_centre_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_prim_health_centre = models.CharField(max_length=2, blank=True, null=True)
    prim_health_subcent_nos = models.IntegerField(blank=True, null=True)
    prim_health_subcent_doct_tot_nos = models.IntegerField(blank=True, null=True)
    prim_health_subcent_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    prim_health_subcent_staff_tot_nos = models.IntegerField(blank=True, null=True)
    prim_health_subcent_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_prim_health_subcent = models.CharField(max_length=2, blank=True, null=True)
    mat_child_wel_centre_nos = models.IntegerField(blank=True, null=True)
    mat_child_wel_centre_doct_tot_nos = models.IntegerField(blank=True, null=True)
    mat_child_wel_centre_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    mat_child_wel_centre_staff_tot_nos = models.IntegerField(blank=True, null=True)
    mat_child_wel_centre_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_mat_child_wel_centre = models.CharField(max_length=2, blank=True, null=True)
    tb_clinic_nos = models.IntegerField(blank=True, null=True)
    tb_clinic_doct_tot_nos = models.IntegerField(blank=True, null=True)
    tb_clinic_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    tb_clinic_staff_tot_nos = models.IntegerField(blank=True, null=True)
    tb_clinic_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_tb_clinic = models.CharField(max_length=2, blank=True, null=True)
    hosp_allopath_nos = models.IntegerField(blank=True, null=True)
    hosp_allopath_doct_tot_nos = models.IntegerField(blank=True, null=True)
    hosp_allopath_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    hosp_allopath_staff_tot_nos = models.IntegerField(blank=True, null=True)
    hosp_allopath_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_hosp_allopath = models.CharField(max_length=2, blank=True, null=True)
    hosp_alt_medicine_nos = models.IntegerField(blank=True, null=True)
    hosp_alt_medicine_doct_tot_nos = models.IntegerField(blank=True, null=True)
    hosp_alt_medicine_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    hosp_alt_medicine_staff_tot_nos = models.IntegerField(blank=True, null=True)
    hosp_alt_medicine_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_hosp_alt_medicine = models.CharField(max_length=2, blank=True, null=True)
    dispensary_nos = models.IntegerField(blank=True, null=True)
    dispensary_doct_tot_nos = models.IntegerField(blank=True, null=True)
    dispensary_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    dispensary_staff_tot_nos = models.IntegerField(blank=True, null=True)
    dispensary_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_dispensary = models.CharField(max_length=2, blank=True, null=True)
    vet_hospital_nos = models.IntegerField(blank=True, null=True)
    vet_hospital_doct_tot_nos = models.IntegerField(blank=True, null=True)
    vet_hospital_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    vet_hospital_staff_tot_nos = models.IntegerField(blank=True, null=True)
    vet_hospital_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_vet_hospital = models.CharField(max_length=2, blank=True, null=True)
    mob_health_clinic_nos = models.IntegerField(blank=True, null=True)
    mob_health_clinic_doct_tot_nos = models.IntegerField(blank=True, null=True)
    mob_health_clinic_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    mob_health_clinic_staff_tot_nos = models.IntegerField(blank=True, null=True)
    mob_health_clinic_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_mob_health_clinic = models.CharField(max_length=2, blank=True, null=True)
    fam_welfare_centre_nos = models.IntegerField(blank=True, null=True)
    fam_welfare_centre_doct_tot_nos = models.IntegerField(blank=True, null=True)
    fam_welfare_centre_doct_inpos_nos = models.IntegerField(blank=True, null=True)
    fam_welfare_centre_staff_tot_nos = models.IntegerField(blank=True, null=True)
    fam_welfare_centre_staff_inpos_nos = models.IntegerField(blank=True, null=True)
    ina_distcode_mob_fam_welfare_centre = models.CharField(max_length=2, blank=True, null=True)
    ngvt_med_fac_out_pat_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_in_out_pat_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_charitable_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_med_practitioner_mbbs_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_med_practitioner_otherdeg_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_med_practitioner_nodeg_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_med_practitioner_faithhealer_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_medicine_shop_nos = models.IntegerField(blank=True, null=True)
    ngvt_med_fac_others_nos = models.IntegerField(blank=True, null=True)
    tap_water_treated_status = models.NullBooleanField()
    tap_water_treated_fn_round_year = models.NullBooleanField()
    tap_water_treated_fn_summer_months = models.NullBooleanField()
    tap_water_untreated_status = models.NullBooleanField()
    tap_water_untreated_fn_round_year = models.NullBooleanField()
    tap_water_untreated_fn_summer_months = models.NullBooleanField()
    cov_well_status = models.NullBooleanField()
    cov_well_fn_round_year = models.NullBooleanField()
    cov_well_fn_summer_months = models.NullBooleanField()
    uncov_well_status = models.NullBooleanField()
    uncov_well_fn_round_year = models.NullBooleanField()
    uncov_well_fn_summer_months = models.NullBooleanField()
    han_pump_status = models.NullBooleanField()
    han_pump_fn_round_year = models.NullBooleanField()
    han_pump_fn_summer_months = models.NullBooleanField()
    tub_wells_borehole_status = models.NullBooleanField()
    tub_wells_fn_round_year = models.NullBooleanField()
    tub_wells_fn_summer_months = models.NullBooleanField()
    spring_status = models.NullBooleanField()
    spring_fn_round_year = models.NullBooleanField()
    spring_fn_summer_months = models.NullBooleanField()
    river_canal_status = models.NullBooleanField()
    river_canal_fn_round_year = models.NullBooleanField()
    river_canal_fn_summer_months = models.NullBooleanField()
    tank_pond_lake_status = models.NullBooleanField()
    tank_pond_lake_fn_round_year = models.NullBooleanField()
    tank_pond_lake_fn_summer_months = models.NullBooleanField()
    others_status = models.NullBooleanField()
    others_fn_round_year = models.NullBooleanField()
    others_fn_summer_months = models.NullBooleanField()
    closed_drainage_status = models.NullBooleanField()
    open_drainage_status = models.NullBooleanField()
    no_drainage_status = models.NullBooleanField(db_column='no _drainage_status')  # Field renamed to remove unsuitable characters.
    op_pucca_drainage_cov_w_tiles_slabs_status = models.NullBooleanField()
    op_pucca_drainage_uncovered_status = models.NullBooleanField()
    op_kuccha_drainage_status = models.NullBooleanField()
    drainage_discharge_status = models.NullBooleanField()
    area_covered_tot_sanitation_campaign_status = models.NullBooleanField()
    com_toilet_complex_w_bath_gen_public = models.NullBooleanField()
    com_toilet_complex_no_bath_gen_public = models.NullBooleanField()
    rural_prod_cent_sanitary_hw_outlet_availability = models.NullBooleanField()
    rural_prod_mart_sanitary_hw_outlet_availability = models.NullBooleanField()
    com_waste_disposal_system = models.NullBooleanField()
    com_biogas_recycle_of_waste = models.NullBooleanField()
    no_system_garbage_onroads = models.NullBooleanField()
    post_office_status = models.NullBooleanField()
    ina_dist_post_office = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    sub_post_office_status = models.NullBooleanField()
    ina_dist_sub_post_office = models.CharField(max_length=2, blank=True, null=True)
    post_telegraph_office_status = models.NullBooleanField()
    ina_dist_post_telegraph_office = models.CharField(max_length=2, blank=True, null=True)
    vil_pin_code_status = models.NullBooleanField()
    ina_dist_vil_pin_code = models.CharField(max_length=2, blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)
    tel_landlines_status = models.NullBooleanField()
    ina_dist_tel_landlines = models.CharField(max_length=2, blank=True, null=True)
    pco_status = models.NullBooleanField()
    ina_dist_pco = models.CharField(max_length=2, blank=True, null=True)
    mob_phone_coverage_status = models.NullBooleanField()
    ina_dist_mob_phone_coverage = models.CharField(max_length=2, blank=True, null=True)
    internet_cafe_status = models.NullBooleanField()
    ina_dist_internet_cafe = models.CharField(max_length=2, blank=True, null=True)
    pri_courier_facility_status = models.NullBooleanField()
    ina_dist_pri_courier_facility = models.CharField(max_length=2, blank=True, null=True)
    pub_bus_service_status = models.NullBooleanField()
    ina_dist_pub_bus_service = models.CharField(max_length=2, blank=True, null=True)
    pri_bus_service_status = models.NullBooleanField()
    ina_dist_pri_bus_service = models.CharField(max_length=2, blank=True, null=True)
    railway_station_status = models.NullBooleanField()
    ina_dist_railway_station = models.CharField(max_length=2, blank=True, null=True)
    auto_modified_autos_status = models.NullBooleanField()
    ina_dist_auto_modified_autos = models.CharField(max_length=2, blank=True, null=True)
    taxi_status = models.NullBooleanField()
    ina_dist_taxi = models.CharField(max_length=2, blank=True, null=True)
    van_status = models.NullBooleanField()
    ina_dist_van = models.CharField(max_length=2, blank=True, null=True)
    tractor_status = models.NullBooleanField()
    ina_dist_tractor = models.CharField(max_length=2, blank=True, null=True)
    cycle_pulled_rickshaws_manual_status = models.NullBooleanField()
    ina_dist_cycle_pulled_rickshaws_manual = models.CharField(max_length=2, blank=True, null=True)
    cycle_pulled_rickshaws_machine_status = models.NullBooleanField()
    ina_dist_cycle_pulled_rickshaws_machine = models.CharField(max_length=2, blank=True, null=True)
    carts_by_animals_status = models.NullBooleanField()
    ina_dist_carts_by_animals = models.CharField(max_length=2, blank=True, null=True)
    sea_river_ferry_service_status = models.NullBooleanField()
    ina_dist_sea_river_ferry_service = models.CharField(max_length=2, blank=True, null=True)
    nat_highway_status = models.NullBooleanField()
    ina_dist_nat_highway = models.CharField(max_length=2, blank=True, null=True)
    state_highway_status = models.NullBooleanField()
    ina_dist_state_highway = models.CharField(max_length=2, blank=True, null=True)
    major_district_road_status = models.NullBooleanField()
    ina_dist_major_district_road = models.CharField(max_length=2, blank=True, null=True)
    oth_district_road_status = models.NullBooleanField()
    ina_dist_oth_district_road = models.CharField(max_length=2, blank=True, null=True)
    black_topped_pucca_road_staus = models.NullBooleanField()
    ina_dist_black_topped_pucca_road = models.CharField(max_length=2, blank=True, null=True)
    gravel_kuchha_roads_status = models.NullBooleanField()
    ina_dist_gravel_kuchha_roads = models.CharField(max_length=2, blank=True, null=True)
    water_bounded_macadam_status = models.NullBooleanField()
    ina_dist_wat_bounded_macadam = models.CharField(max_length=2, blank=True, null=True)
    all_weather_road_status = models.NullBooleanField()
    ina_dist_all_weather_road = models.CharField(max_length=2, blank=True, null=True)
    navigable_waterways_river_canal_status = models.NullBooleanField()
    ina_dist_navigable_waterways_river_canal = models.CharField(max_length=2, blank=True, null=True)
    footpath_status = models.NullBooleanField()
    ina_dist_footpath = models.CharField(max_length=2, blank=True, null=True)
    atm_status = models.NullBooleanField()
    ina_dist_atm = models.CharField(max_length=2, blank=True, null=True)
    commercial_bank_status = models.NullBooleanField()
    ina_dist_commercial_bank = models.CharField(max_length=2, blank=True, null=True)
    cooperative_bank_status = models.NullBooleanField()
    ina_dist_cooperative_bank = models.CharField(max_length=2, blank=True, null=True)
    agri_credit_societies_status = models.NullBooleanField()
    ina_dist_agri_credit_societies = models.CharField(max_length=2, blank=True, null=True)
    selfhelp_group_status = models.NullBooleanField()
    ina_dist_selfhelp_group = models.CharField(max_length=2, blank=True, null=True)
    public_distribution_system_status = models.NullBooleanField()
    ina_dist_public_distribution_system = models.CharField(max_length=2, blank=True, null=True)
    mandis_regular_market_status = models.NullBooleanField()
    ina_dist_mandis_regular_market = models.CharField(max_length=2, blank=True, null=True)
    weekly_haat_status = models.NullBooleanField()
    ina_dist_weekly_haat = models.CharField(max_length=2, blank=True, null=True)
    agri_marketing_society_status = models.NullBooleanField()
    ina_dist_agri_marketing_society = models.CharField(max_length=2, blank=True, null=True)
    nutritional_centres_icds_status = models.NullBooleanField()
    ina_dist_nutritional_centres_icds = models.CharField(max_length=2, blank=True, null=True)
    nutritional_centres_anganwadi_status = models.NullBooleanField()
    ina_dist_nutritional_centres_anganwadi = models.CharField(max_length=2, blank=True, null=True)
    nutritional_centres_others_status = models.NullBooleanField()
    ina_dist_nutritional_centres_others = models.CharField(max_length=2, blank=True, null=True)
    asha_status = models.NullBooleanField()
    ina_dist_asha = models.CharField(max_length=2, blank=True, null=True)
    community_centre_with_tv = models.NullBooleanField()
    ina_dist_community_centre_with_tv = models.CharField(max_length=2, blank=True, null=True)
    sports_field_status = models.NullBooleanField()
    ina_dist_sports_field = models.CharField(max_length=2, blank=True, null=True)
    sports_club_status = models.NullBooleanField()
    ina_dist_sports_club = models.CharField(max_length=2, blank=True, null=True)
    cinema_video_hall_status = models.NullBooleanField()
    ina_dist_cinema_video_hall = models.CharField(max_length=2, blank=True, null=True)
    public_library_status = models.NullBooleanField()
    ina_dist_public_library = models.CharField(max_length=2, blank=True, null=True)
    pub_reading_room_status = models.NullBooleanField()
    ina_dist_pub_reading_room = models.CharField(max_length=2, blank=True, null=True)
    daily_newspaper_supply_status = models.NullBooleanField()
    ina_dist_daily_newspaper_supply = models.CharField(max_length=2, blank=True, null=True)
    assembly_polling_station_status = models.NullBooleanField()
    ina_dist_assembly_polling_station = models.CharField(max_length=2, blank=True, null=True)
    birth_death_registration_office = models.NullBooleanField()
    ina_dist_birth_death_registration_office = models.CharField(max_length=2, blank=True, null=True)
    power_supply_dom_use = models.NullBooleanField()
    power_supply_dom_use_summer_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_dom_use_winter_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_agri_use = models.NullBooleanField()
    power_supply_agri_use_summer_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_agri_use_winter_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_comm_use = models.NullBooleanField()
    power_supply_comm_use_summer_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_comm_use_winter_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_for_all_users = models.NullBooleanField()
    power_supply_for_all_users_summer_hrspd = models.IntegerField(blank=True, null=True)
    power_supply_for_all_users_winter_hrspd = models.IntegerField(blank=True, null=True)
    agri_commodities_first = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    manufacturers_commodities_first = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    handicrafts_commodities_first = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    agri_commodities_second = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    manufacturers_commodities_second = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    handicrafts_commodities_second = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    agri_commodities_third = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    manufacturers_commodities_third = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    handicrafts_commodities_third = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    forest_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    non_agri_use_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    barren_uncoltivable_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    permanent_pastures_other_grazing_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    land_misc_tree_crops_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    culturable_wasteland_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    fallows_land_otherthan_current_fallows_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    current_fallows_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    net_area_sown = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    tot_unirrigatedland_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    area_irrigated_by_source = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    canals_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    wells_tube_wells_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    tanks_lakes_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    waterfall_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    other_source_area = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    nearest_town_name = models.CharField(max_length=30, blank=True, null=True)  # This field type is a guess.
    dist_nearest_town = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'census_rest'